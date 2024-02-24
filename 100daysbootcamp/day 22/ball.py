from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.y = 10
        self.x = 10
        self.pace = 0.1
    def move_ball(self):
        
        self.x_pos  = self.xcor() + self.x
        self.y_pos = self.ycor() + self.y
        self.goto(self.x_pos, self.y_pos)
        

    def bounce_y(self):
        self.y *= -1
    
    def bounce_x(self):
        self.x *= -1
        self.pace *=0.9
        
        
        
    
    def reset_position(self):
        self.goto(0,0)
        self.pace = 0.1
        self.bounce_x()