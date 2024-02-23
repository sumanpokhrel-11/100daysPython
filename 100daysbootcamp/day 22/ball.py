from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.penup()
        
    def move_ball(self):
        while True:
            self.forward(5)