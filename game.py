import board_game as bg

num_players = raw_input("How Many Teams? ")

game = bg.Game(num_players)
players = game.get_players()
Level_One_Winner = game.level_one(players)
