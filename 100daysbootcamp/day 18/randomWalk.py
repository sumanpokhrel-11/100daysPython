from turtle import Turtle, Screen
import turtle as tt
import random
t = Turtle()
t.shape('turtle')
t.color("red","green")
t.screen.title("Random Walk Using Turtle")
t.screen.bgcolor("yellow")

tt.colormode(255)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    return (r, g, b)
# listColor = ['Red', 'DarkOrchid', 'CornflowerBlue', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
directions = [0, 90, 180, 270]
t.pensize(11)
t.speed('fastest')

for _ in range(300):
    t.color((randomColor()))
    t.forward(25)
    t.setheading(random.choice(directions))

t.hideturtle()

screen = Screen()
screen.exitonclick()
