from turtle import Turtle, Screen
myTurtle = Turtle()

myTurtle.shape('turtle')
myTurtle.speed('slow')
myTurtle.color('red', 'green')
for _ in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)
    



screen = Screen()
screen.exitonclick()
