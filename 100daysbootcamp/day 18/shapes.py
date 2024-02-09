from turtle import Turtle, Screen
import random
t = Turtle()
t.shape('turtle')
t.color("red","green")
t.screen.title("Different Geometric Shapes")
t.screen.bgcolor("yellow")


listColor = ['Red', 'DarkOrchid', 'CornflowerBlue', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
def drawShape(side):

    angle = 360/side
    for _ in range(side):
        t.forward(100)
        t.right(angle)


for shapeSide in range(3, 11):
    t.color(random.choice(listColor))
    drawShape(shapeSide)






s = Screen()
s.exitonclick()