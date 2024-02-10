import turtle as t
import random
from turtle import Turtle, Screen

sam = Turtle()
t.colormode(255)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    return (r, g, b)

sam.speed('fastest')
sam.pensize('3')
sam.screen.title("Spirograph Using Turtle")
def drawSpiral(no_of_spaces):
    for _ in range(int(360/no_of_spaces)):
        sam.color(randomColor())
        sam.circle(150)
        sam.setheading(sam.heading() + no_of_spaces)

drawSpiral(6)
screen = Screen()
screen.exitonclick()