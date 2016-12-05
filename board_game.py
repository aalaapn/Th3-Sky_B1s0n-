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
CLASSICS_QUESTIONS  =   DATA.get_classics()
NUM_CLASSICS        =   len(CLASSICS_QUESTIONS)

class Team:
    def __init__(self, name, score, level, first):
        self.score = score
        self.name = name
        self.level = level
        self.first = first

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_level(self):
        return self.level

    def gain_point(self):
        self.score +=1

    def update_level(self):
        if (self.score >= 10):
            self.level = 2
        elif (self.score >= 20):
            self.level = 3
        elif (self.score >= 25):
            self.level = 4
        elif (self.score >= 30):
            self.level = 5
        elif (self.score  >= 35):
            self.level = 6

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
            team_n = Team(team_name_n, 0, 1, [0,0,0,0,0])
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
    def level_one(self, names, team_number):
        self.names = names
        self.team_number = team_number
        dice_roll   = random.randrange(0,len(DATA.get_cat_level_one()))
        print self.names[self.team_number].get_name() + " your turn to play!!!"
        if(self.names[self.team_number].first[0] == 0):
            user_input.get_yes_no("Ready for Level One? " + self.names[self.team_number].get_name())

            ascii_art.hash()
            ascii_art.level_one_text()
            ascii_art.hash()
            self.names[self.team_number].first[0] = 1
        game = self.pick_game(DATA.get_cat_level_one())
        ascii_art.small_space()
        print self.names[self.team_number].get_name() + " " + " trivia time"
        index = random.randrange(0,NUM_TRIVIA)
        question = TRIVIA_QUESTIONS[index]
        print question
        done = raw_input("Did you answer the question? [y/n] ")
        answer = TRIVIA_ANSWERS[index]
        print answer
        result_of_question = raw_input("Did you get the question right? [y/n] ")
        if(result_of_question == 'y'):
            self.names[self.team_number].gain_point()
        self.names[self.team_number].update_level()
        if(self.names[self.team_number].get_score() == 10):
            ascii_art.end_level_one_text()



    def level_two(self, names, team_number):
        self.names = names
        self.team_number = team_number
        dice_roll   = random.randrange(0,len(DATA.get_cat_level_one()))
        print self.names[self.team_number].get_name() + " your turn to play!!!"
        if(self.names[self.team_number].first[1] == 0):
            user_input.get_yes_no("Ready for Level Two? " + self.names[self.team_number].get_name())

            ascii_art.hash()
            ascii_art.level_two_text()
            ascii_art.hash()
            self.names[self.team_number].first[1] = 1
        game = self.pick_game(DATA.get_cat_level_one())
        ascii_art.small_space()
        print self.names[self.team_number].get_name() + " " + " your catagory is : " + DATA.get_cat_level_one()[game]

        if (DATA.get_cat_level_one()[game] == 'SQ'):
            print 'SQ'
        elif (DATA.get_cat_level_one()[game] == 'Artistry'):
            print 'Artistry'
            index = random.randrange(0,4)
            art = ARTISTRY_QUESTIONS[index]
            print art
        elif (DATA.get_cat_level_one()[game] == 'Chance'):
            print 'Chance'
            index = random.randrange(0,4)
            chance = CHANCE_QUESTIONS[index]
            print chance
        elif (DATA.get_cat_level_one()[game] == 'Puzzle'):
            print 'Puzzle'
            index = random.randrange(0,4)
            puzz = PUZZLE_QUESTIONS[index]
            print puzz

        result_of_question = int(raw_input("number of team that won the point "))

        self.names[result_of_question].gain_point()
        self.names[result_of_question].update_level()
        if(self.names[self.team_number].get_score() == 20):
            ascii_art.end_level_one_text()


    def level_three(self, names, team_number):
        self.names = names
        self.team_number = team_number
        dice_roll   = random.randrange(0,len(DATA.get_cat_level_one()))
        print self.names[self.team_number].get_name() + " your turn to play!!!"
        if(self.names[self.team_number].first[2] == 0):
            user_input.get_yes_no("Ready for Level Two? " + self.names[self.team_number].get_name())

            ascii_art.hash()
            ascii_art.level_three_text()
            ascii_art.hash()
            self.names[self.team_number].first[2] = 1
        index = random.randrange(0,4)
        classic = CLASSICS_QUESTIONS[index]
        print classic
        result_of_question = int(raw_input("number of team that won the point "))

        self.names[result_of_question].gain_point()
        self.names[result_of_question].update_level()
        if(self.names[self.team_number].get_score() == 25):
            ascii_art.end_level_one_text()


    def level_four(self, names, team_number):
        self.names = names
        self.team_number = team_number
        dice_roll   = random.randrange(0,len(DATA.get_cat_level_one()))
        print self.names[self.team_number].get_name() + " your turn to play!!!"
        if(self.names[self.team_number].first[3] == 0):
            user_input.get_yes_no("Ready for Level Two? " + self.names[self.team_number].get_name())

            ascii_art.hash()
            ascii_art.level_four_text()
            ascii_art.hash()
            self.names[self.team_number].first[3] = 1
        index = random.randrange(0,28)
        body = BODY_QUESTIONS[index]
        print body
        result_of_question = int(raw_input("number of team that won the point "))

        self.names[result_of_question].gain_point()
        self.names[result_of_question].update_level()
        if(self.names[self.team_number].get_score() == 30):
            ascii_art.end_level_one_text()

    def level_five(self, names, team_number):
        self.names = names
        self.team_number = team_number
        dice_roll   = random.randrange(0,len(DATA.get_cat_level_one()))
        print self.names[self.team_number].get_name() + " your turn to play!!!"
        if(self.names[self.team_number].first[4] == 0):
            user_input.get_yes_no("Ready for Level Two? " + self.names[self.team_number].get_name())

            ascii_art.hash()
            ascii_art.level_five_text()
            ascii_art.hash()
            self.names[self.team_number].first[4] = 1
        index = random.randrange(0,25)
        spirit = SPIRIT_QUESTIONS[index]
        print spirit
        result_of_question = int(raw_input("number of team that won the point "))

        self.names[result_of_question].gain_point()
        self.names[result_of_question].update_level()
        if(self.names[self.team_number].get_score() == 35):
            ascii_art.end_level_one_text()
