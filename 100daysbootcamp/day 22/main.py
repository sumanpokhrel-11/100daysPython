from turtle import Turtle, Screen
from ball import Ball
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

paddle = Turtle()
paddle.shape('square')
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.setposition(350,0)

def go_up():
    new_y = paddle.ycor() + 20 # to move up by 20 pixels
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20 # to move down by 20 pixels
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up,'Up')
screen.onkey(go_down,'Down')

game_on = True
while game_on:
    ''' using screen tracer stops 
    the animations and using update, updates the screen '''
    screen.update()


# ball = Ball()
# ball.move_ball()
screen.exitonclick()