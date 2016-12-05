import random
import user_input
import ascii_art as ascii_art
import google_sheets_questions_backend as qdata

#constants
DATA = qdata.data()
TRIVIA_QUESTIONS    =   DATA.get_trivia_questions()
TRIVIA_ANSWERS      =   DATA.get_trivia_answers()
NUM_TRIVIA          =   len(TRIVIA_QUESTIONS)
ARTISTRY_QUESTIONS  =   DATA.get_artistry()
NUM_ARTISTRY        =   len(ARTISTRY_QUESTIONS)
CHANCE_QUESTIONS    =   DATA.get_chance()
NUM_CHANCE          =   len(CHANCE_QUESTIONS)
PUZZLE_QUESTIONS    =   DATA.get_puzzle()
NUM_PUZZLE          =   len(PUZZLE_QUESTIONS)
BODY_QUESTIONS      =   DATA.get_body()
NUM_BODY            =   len(BODY_QUESTIONS)
SPIRIT_QUESTIONS    =   DATA.get_spirit()
NUM_SPIRIT          =   len(SPIRIT_QUESTIONS)

class Team:
    def __init__(self, name, score):
        self.score = score
        self.name = name

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def gain_point(self):
        self.score +=1

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
            team_name_n  = raw_input('Enter your name Team '  + str(n) + ': ')
            team_n = Team(team_name_n, 0)
            ascii_art.small_space()
            ascii_art.hash()
            print "Welcome " + team_n.get_name()
            ascii_art.hash()
            ascii_art.small_space()
            names.append(team_n)
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
        winner = False
        self.names = names
        for n in range(int(self.num_teams)):
            user_input.get_yes_no("Ready for Level One? " + self.names[n].get_name())
        dice_roll   = random.randrange(0,len(DATA.get_cat_level_one()))

        ascii_art.hash()
        ascii_art.level_one_text()
        ascii_art.hash()

        while(!winner):
            for n in range(int(self.num_teams)):
                print self.names[n].get_name() + "your turn to play!!!"
                game = self.pick_game(DATA.get_cat_level_one())
                ascii_art.small_space()
                print self.names[n].get_name() + " " + " your catagory is : " + DATA.get_cat_level_one()[game]

                if (DATA.get_cat_level_one()[game] == 'Trivia'):

                elif (DATA.get_cat_level_one()[game] == 'Artistry'):
                    print 'Artistry'
                elif (DATA.get_cat_level_one()[game] == 'Chance'):
                    print 'Chance'
                elif (DATA.get_cat_level_one()[game] == 'Puzzle'):
                    print 'Puzzle'
        ascii_art.end_level_one_text()



    def level_two(self, names):
        self.names = names

    def level_three(self, names):
        self.names = names

    def level_four(self, names):
        self.names = names

    def level_five(self, names):
        self.names = names
