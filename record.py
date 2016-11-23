#code take from pyAudio Documentation and Examples
# http://people.csail.mit.edu/hubert/pyaudio/
#

import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = .03
WAVE_OUTPUT_FILENAME = "output.wav"

frames = []
for x in range(10):
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
t = np.arange((sig.size)/2)
freq = np.fft.fftfreq(t.shape[-1])

raw_right = np.array([])
raw_left = np.array([])
sp_right = np.array([])
sp_left  = np.array([])
for s in range(sig.size/2):
   raw_right    =   np.append(raw_right, sig[s][0])
   raw_left     =   np.append(raw_left, sig[s][1])
   sp_right     =   np.append(sp_right, sp[s][0])
   sp_left      =   np.append(sp_left, sp[s][1])


plt.plot(freq, sp.real, freq, sp.imag)
plt.show()


wf.close()
