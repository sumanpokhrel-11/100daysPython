import turtle
import pandas as pd
screen = turtle.Screen()
image = ('100daysbootcamp\day 25\image.gif')
screen.addshape(image)
screen.title("US-State Quiz")
turtle.shape(image)


state = pd.read_csv('100daysbootcamp\day 25\states.csv')
counter = 0
state_name = state['state'].to_list()
answer_collection = []
game_is_on = True
while len(answer_collection)< 50:
    answer = screen.textinput(title=f'{counter}/50 States are Correct', prompt= "Enter another state name: ")
    answer = answer.capitalize()
    

    # checking if the answer is in the list of state_name
    if answer in state_name:
        state_data = state[state['state'] == answer]
        answer_collection.append(answer)
        sam = turtle.Turtle()
        sam.penup()
        sam.hideturtle()
        sam.goto(int(state_data.x), int(state_data.y))
        sam.write(answer)
        counter +=1

    if answer not in state_name:
        game_is_on = False

screen.exitonclick()

# data = pd.read_csv('100daysbootcamp\day 25\squirrel_data.csv')
# gray_squirrel = len(data[data['Primary Fur Color']=='Gray'])
# black_squirrel = len(data[data['Primary Fur Color']=='Black'])
# cinnamon_squirrel = len(data[data['Primary Fur Color']=='Cinnamon'])

# print(gray_squirrel)

# dict_squirrel = {
#     'color' :['gray', 'black', 'cinnamon'],
#     'count' : [gray_squirrel, black_squirrel, cinnamon_squirrel]
# }
# df = pd.DataFrame(dict_squirrel)
# df.to_csv('100daysbootcamp/day 25/color_squirrel.csv')
# data = pd.read_csv('100daysbootcamp/day 25/color_squirrel.csv')
# print(data)