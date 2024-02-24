from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 40, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0


    def write_score(self):

        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.l_score}', align =ALIGN , font=FONT)

        self.goto(100, 200)
        self.write(f'{self.r_score}', align =ALIGN , font=FONT)
        
    def score_l(self):
        self.l_score +=1
        self.write_score()

    def score_r(self):
        self.r_score +=1
        self.write_score()