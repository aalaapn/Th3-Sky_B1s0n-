import board_game as bg
Winner = False
num_players = raw_input("How Many Teams? ")

game = bg.Game(num_players)
teams = game.get_players()
game.level_one(players, 0)


while(Winner):
    itr = 1
    for team in teams:
        if (team.score >= 10):
            game.level_two(teams, team)
        elif (team.score >= 20):
            game.level_two(teams, team)
        elif (team.score >= 25):
            game.level_two(teams, team)
        elif (team.score >= 30):
            game.level_two(teams, team)
        elif (team.score  >= 35):
            game.level_two(teams, team)
        else:
            game.level_one(teams, team)

        if(team.get_level() == 6)
            Winner = False

        print team.get_name()
        print team.get_level()
        print team.get_score()

print("go study")
