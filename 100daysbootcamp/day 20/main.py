from turtle import Screen
from snake import Snake
from food import Food
import time
'''setting up the screen'''
screen = Screen()
screen.setup(width=600 ,height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = Food()
'''setting up the key handler i.e arrows handles the directions'''
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


#detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
   

screen.exitonclick()