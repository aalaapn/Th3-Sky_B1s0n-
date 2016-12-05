import board_game as bg
Winner = True
num_players = raw_input("How Many Teams? ")

game = bg.Game(num_players)
teams = game.get_players()



while(Winner):
    itr = 0
    for team in teams:
        if (team.score < 10):
            game.level_one(teams, itr)
        elif (team.score >= 10):
            game.level_two(teams, itr)
        elif (team.score >= 20):
            game.level_three(teams, itr)
        elif (team.score >= 25):
            game.level_four(teams, itr)
        elif (team.score >= 30):
            game.level_five(teams, itr)
        elif (team.score  >= 35):
            print('poop')

        if(team.get_level() == 6):
            Winner = False

        print team.get_name()
        print team.get_level()
        print team.get_score()

        itr += 1

print("go study")
