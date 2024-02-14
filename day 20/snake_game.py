from turtle import Turtle, Screen
import random
screen = Screen()
# screen.tracer()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
zero_snake = []
x = 0
positions = [(0,0), (-20.0, 0.00), (-40.00, 0.00)]
for _ in range(3):
    sam = Turtle()
    sam.penup()
    sam.shape('square')
    sam.color('white')
    sam.goto(x, 0)
    zero_snake.append(sam)
    x +=20
move_snake = True
while move_snake:
    for position in positions(2, 1, 1):
        pass
    


    # for snake in zero_snake:
    #     snake.forward(5)






screen.exitonclick()