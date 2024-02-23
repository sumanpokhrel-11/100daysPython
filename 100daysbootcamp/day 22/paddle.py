from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()

        
        self.shape('square')
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.goto(x_pos, y_pos)
        self.speed('fastest')
    def go_up(self):
        '''this method moves the paddle to upward by 20 pixels'''

        new_y = self.ycor() + 20 # to move up by 20 pixels
        self.goto(self.xcor(), new_y)
    def go_down(self):
        '''this method moves the paddle to downward by 20 pixels'''

        new_y = self.ycor() - 20 # to move down by 20 pixels
        self.goto(self.xcor(), new_y)
