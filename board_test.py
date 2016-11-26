import board_game as bg
import user_input as yn


import google_sheets_questions_backend as qdata

levels = []
cat_level_one = []
cat_level_two = []
cat_level_three = []
data = qdata.data(levels, cat_level_one, cat_level_two, cat_level_three)
data.get_cat_level_one()
print cat_level_one
