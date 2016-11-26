import random
import user_input
import ascii_art as ascii_art
import google_sheets_questions_backend as qdata
DATA = qdata.data()
class Team:
    def __init__(self, score):
        self.score = score
        
    def gain_point():
        self.score +=1

    def get_score():
        return self.score

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
            ascii_art.small_space()
            ascii_art.hash()
            print "Welcome " + player_n
            ascii_art.hash()
            ascii_art.small_space()
            names.append(player_n)
        return names

    ##############################
    #actions
    ##############################
    def roll_dice(self):
        dice_roll = random.randrange(6)
        return dice_roll

    def pick_game(self, games):
        num_games = len(games)
        return random.randrange(0, num_games)

    ##############################
    #levels
    ##############################
    def level_one(self, names):
        self.names = names
        for n in range(int(self.num_teams)):
            user_input.get_yes_no("Ready for Level One? " + self.names[n])
        dice_roll   = random.randrange(0,len(DATA.get_cat_level_one()))

        ascii_art.hash()
        ascii_art.level_one_text()
        ascii_art.hash()

        while(1):
            for n in range(int(self.num_teams)):
                print self.names[n] + "your turn to play!!!"
                game = self.pick_game(DATA.get_cat_level_one())
                ascii_art.small_space()
                print self.names[n] + " " + " your catagory is : " + DATA.get_cat_level_one()[game]
                if (DATA.get_cat_level_one()[game] == 'Trivia'):
                    print 'trivia'
                elif (DATA.get_cat_level_one()[game] == 'Artistry'):
                    print 'Artistry'
                elif (DATA.get_cat_level_one()[game] == 'Chance'):
                    print 'Chance'
                elif (DATA.get_cat_level_one()[game] == 'Puzzle'):
                    print 'Puzzle'



    def level_two(self, names):
        self.names = names

    def level_three(self, names):
        self.names = namess
