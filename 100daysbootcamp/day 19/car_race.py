from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 800, height = 800)
bet = screen.textinput(title='Bet a Car', prompt='Which color car wins the race?: ')
y = 0
start_race = False
if bet:
    start_race = True
turtles = []
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
for i in range(len(colors)):
    sam = Turtle()
    sam.penup()
    sam.shape('turtle')
    sam.color(colors[i])
    sam.goto(-350,-300 + y)
    y +=100
    turtles.append(sam)
    

no_winner = True
while start_race:
    for turtle in turtles:
        if turtle.xcor() > 400:
            start_race = False
            winner = turtle.pencolor()
            if winner ==bet:
                print("You have Won")
                turtle.write("Winner")
            else:
                print("Loser")
                turtle.write("Loser")

        turtle.forward(random.randint(0,10))


screen.exitonclick()