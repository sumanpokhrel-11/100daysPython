from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.y = 0.2
        self.x = 0.2
    def move_ball(self):
        
        self.x_pos  = self.xcor() + self.x
        self.y_pos = self.ycor() + self.y
        self.goto(self.x_pos, self.y_pos)
        

    def bounce_y(self):
        self.y *= -1
    
    def bounce_x(self):
        self.x *= -1