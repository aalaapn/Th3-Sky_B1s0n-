import random

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
    ##############################
    #game initialization
    ##############################
    def get_num_players(self):
        return self.num_players

    def get_players(self):
        names = []
        for n in range(self.num_players):
            player_n  = raw_input('Enter your name player'  + str(n) + ': ')
            names.append(player_n)
            return names
        print ("Thank You!")

    ##############################
    #actions
    ##############################
    def roll_dice(self):
        dice_roll = random.randrange(6)
        return dice_roll

    ##############################
    #levels
    ##############################
    def level_one (Mind):
        trivia      = 0
        artistry    = 1
        chance      = 2
        puzzle      = 3
        dice_roll   = random.randrange(0,3)
