from turtle import Turtle, Screen
import turtle as tt
import random

tim = Turtle()
tim.speed("fastest")
tt.colormode(255)
tim.hideturtle()
tim.penup() # pull the pen up so that it doesn't draw anything while moving forward

def randomColor():
    '''generates random color and return the tuple of RGB'''
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    return (r, g, b)
tim.pensize(10)


def paint():
    '''paints the horizontal position of the pen with 10 dots'''
    for _ in range (10):
        tim.dot(25, randomColor()) #create a dot of randomcolor of size 25
        tim.forward(50) # the pen is shifted forward by 50 pixel

y = 0.00
for _ in range(10):
    position = (-200.00,-200 + y)
    tim.setposition(position) #changing the vertical position keeping the horizontal position fixed
    paint()
    y +=50.00


screen = Screen()
screen.exitonclick()
