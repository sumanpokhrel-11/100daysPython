from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 20, 'bold')
FONT_GO = ('Arial', 50, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        '''update scoreboard'''
        self.clear()
        with open('100daysbootcamp\day 20\high_score.txt', 'r') as op:
            my_score = op.read()
            self.high_score= int(my_score)
        self.write(f'Score : {self.score}  High Score: {self.high_score}', align=ALIGN, font=FONT)
        
        
    def increase_score(self):
        self.score +=1
        
        self.write_score()

    def game_reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("100daysbootcamp\day 20\high_score.txt",'w') as hiscore:
                hiscore.write(str(self.high_score))
        self.score = 0
        self.write_score()
    
