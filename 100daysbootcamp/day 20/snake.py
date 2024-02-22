from turtle import Turtle
INITIAL_SEGMENT = [(0,0), (-20, 0), (-40,0)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.initial_snake = []
        self.creating_snake()
        self.head = self.initial_snake[0]
    def creating_snake(self):
        '''this function create a snake of 3 square shape'''
        # x, y = -40, 0
        for initial in INITIAL_SEGMENT:
            self.add_snake(initial)

    def add_snake(self, initial):
        '''create new piece for the snake'''
        sam = Turtle('square')
        sam.penup()
        sam.color('white')
        sam.goto(initial)
        # sam.goto(x,y)
        # x +=20
        self.initial_snake.append(sam)

    def extend(self):
        '''add the new piece at last of the previous snake'''
        self.add_snake(self.initial_snake[-1].position())

    def move_snake(self):
        '''
this functions moves the snake'''
        for seg in range(len(self.initial_snake)-1, 0, -1):
            new_x = self.initial_snake[seg-1].xcor()
            new_y = self.initial_snake[seg-1].ycor()
            self.initial_snake[seg].goto(new_x, new_y)
        self.head.forward(SPEED)
        # initial_snake[0].left(90)

       
    '''
    these are the functions for moving the buttons and these stops moving
    directly to opposite direction i.e moving right to left directly is opposed
'''
   

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
