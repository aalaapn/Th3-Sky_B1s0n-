


import google_sheets_questions_backend as qdata

levels = []
cat_level_one = []
cat_level_two = []
cat_level_three = []
data = qdata.data()

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]

cat_level_one = data.get_cat_level_one()
trivia_questions = data.get_trivia_questions()
trivia_answers = data.get_trivia_answers()
a = data.get_artistry()
b = data.get_chance()
c = data.get_puzzle()
d = data.get_body()
e = data.get_spirit()

for x in e:
    print x
