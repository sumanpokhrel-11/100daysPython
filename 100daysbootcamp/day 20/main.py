from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600 ,height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


snake_alive = True
while snake_alive:
    screen.update()
    time.sleep(0.09)    
    snake.move_snake()        

   

screen.exitonclick()