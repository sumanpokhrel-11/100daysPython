from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from score_board import Score
ball = Ball()
screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
paddle_r = Paddle(350,0)
paddle_l = Paddle(-350,0)

score = Score()
screen.listen()
#for right paddle, the controller will be arrow up and down
screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')

#for left paddle, the controller will be key w for up and s for down
screen.onkey(paddle_l.go_up, 'w')
screen.onkey(paddle_l.go_down, 's')



game_on = True
while game_on:
    ''' using screen tracer stops 
    the animations and using update, updates the screen '''
    screen.update()
    ball.move_ball()

# if the ball hit the top or buttom of the screen
# so detecting the collison with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()



# detecting collison with paddle
    if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # detecting the paddle missing the ball
    if ball.xcor()>400:
        ball.reset_position()

    if ball.xcor()<-400:
        ball.reset_position()

    
screen.exitonclick()