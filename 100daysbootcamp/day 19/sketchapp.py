from turtle import Turtle, Screen
sam = Turtle()
screen = Screen()



sam.write('''
w = forward
s = backward
a = counter-clockwise
d = clockwise
''', align='right')
def forward():
    sam.forward(10)
def backward():
    sam.backward(10)
def turn_left():
    sam.left(10)
def turn_right():
    sam.right(10)
def origin():
    sam.clear()
    sam.home()



'''
w = forward
s = backward
a = counter-clockwise
d = clockwise
'''
screen.listen()
screen.onkey(fun= backward, key='s')
screen.onkey(fun=forward, key='w')

screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')




screen.exitonclick()