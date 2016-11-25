import random
<<<<<<< HEAD
import user_input
import ascii_art.py as ascii_art

SPACE = ". \n . . . . .  \n . . . . .  \n . . . . .  \n . . . . .  \n . . . . . \n"
=======
SPACE = "\n . . . . .  \n . . . . .  \n . . . . .  \n . . . . .  \n . . . . . \n"
>>>>>>> af5afc14297eb46324b0ede2208db656f43b4ba9
HASH = "############################################################"
class Game:
    def __init__(self, num_teams):
        self.num_teams = num_teams


    #############################
    #game initialization
    ##############################
    def get_num_teams(self):
        return self.num_teams

    def get_players(self):
        names = []
        for n in range(int(self.num_teams)):
            player_n  = raw_input('Enter your name Team '  + str(n) + ': ')
            print "Welcome " player_n
            print SPACE
            names.append(player_n)
        return names

    ##############################
    #actions
    ##############################
    def roll_dice(self):
        dice_roll = random.randrange(6)
        return dice_roll

    def pick_game(self, games):
        num_games = len(games) -1
        return random.randrange(0, num_games)


    ##############################
    #levels
    ##############################
    def level_one(self, names):
        self.names = names
        games =  [  "trivia",
                    "artistry",
                    "chance",
                    "puzzle",]
        dice_roll   = random.randrange(0,len(games))
        print HASH
        ascii_art.level_one_text()
        print HASH
        for n in range(int(self.num_teams)):
            game = self.pick_game(games)
            print SPACE
            print self.names[n] + " " + " your game is : " + games[dice_roll]

    def level_two(self, names):
        self.names = names

    def level_three(self, names):
        self.names = namess
