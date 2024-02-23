from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 20, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(f'Left Score = {self.l_score}, Right Score is {self.r_score}', align =ALIGN , font=FONT)
        
    def score_l(self):
        self.l_score +=1
    def score_r(self):
        self.r_score +=1