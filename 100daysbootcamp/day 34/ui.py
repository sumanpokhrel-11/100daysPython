from tkinter import *

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score:',fg='white', font=('Arial', 15, 'bold'), bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,bg='white')
        self.question_text = self.canvas.create_text(150, 125, 
                                                     text='Some Questions here!!', 
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, 'italic'))
        
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # correct tick ✅
        self.right_btn = Button(text="✅", font=(40))
        self.right_btn.config(highlightthickness=0, bg='green')
        self.right_btn.grid(row=2, column=0)
        # wrong tick button❌
        self.wrong_btn = Button(text="❌", font=(40))
        self.wrong_btn.config(highlightthickness=0, bg="red")
        self.wrong_btn.grid(row=2, column=1)
        self.window.mainloop()



    def get_next_qn(self):
        self.quiz.next_question