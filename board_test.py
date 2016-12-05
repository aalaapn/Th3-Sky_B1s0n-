import board_game as bg
Winner = False


game = bg.Game(1)
teams = game.get_players()
while(1):
    game.level_two(teams, 0)
