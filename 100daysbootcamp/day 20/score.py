from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 20, 'bold')
FONT_GO = ('Arial', 50, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.hideturtle()
        self.write_score()
    def write_score(self):
        self.write(f'Score : {self.score}', align=ALIGN, font=FONT)
        
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGN, font=FONT_GO)

