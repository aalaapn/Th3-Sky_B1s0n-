import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyaudio
import wave



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = .03
WAVE_OUTPUT_FILENAME = "output_real_time.wav"

#ser=serial.Serial('COM4', 115200)
class Scope(object):
    def __init__(self, ax, maxt=2, dt=.0005, color='b'):
        self.ax = ax
        self.dt = dt
        self.color=color
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(0, 4000)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            #self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        self.line.set_color(np.random.rand(3,1))
        return self.line,

def intTest(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def parse(str):
    returnInts=[]
    str=str.partition(' ')
    str=str[2]
    while(str!=''):
        str=str.partition(' ')
        c=str[0]
        str=str[2]
        if(intTest(c)):
            returnInts.append(int(c))
    return returnInts

def data1():
    frames = []

    while True:
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

        print("* recording")

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

        sig = np.frombuffer(data, dtype='<i2').reshape(-1, CHANNELS)
        sp = np.fft.fft(sig)
        frames = []
        yield np.abs(sp[0][0])


fig, ax = plt.subplots(1, 1, sharey=True)
fig.facecolor='black'
ax.set_title('Accelerometer x data')

scope = Scope(ax,2, .05,'r')



#pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(fig, scope.update, data1, interval=.0001,
                              blit=True)


plt.show()
