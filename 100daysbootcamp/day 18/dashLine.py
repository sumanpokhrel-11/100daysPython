from turtle import Turtle, Screen
myTurtle = Turtle()


myTurtle.screen.title("My Turtle Graphical Images or Graphics") #this line display the title of the screen
myTurtle.screen.bgcolor('yellow')
myTurtle.shape('turtle')
myTurtle.speed('slow')
myTurtle.color('red', 'green')


for _ in range(10):
    myTurtle.forward(5)
    myTurtle.penup()
    myTurtle.forward(5)
    myTurtle.pendown()


# Creating a circle using Turtle
# myTurtle.color("black", "red")
# myTurtle.begin_fill()
# myTurtle.circle(80)
# myTurtle.end_fill()
# myTurtle.hideturtle() #this line hides the turtle or make it invisible





screen = Screen()
screen.exitonclick()
