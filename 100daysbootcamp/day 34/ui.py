from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score:',fg='white', font=('Arial', 15, 'bold'), bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,bg='white')
        self.question_text = self.canvas.create_text(150, 125, 
                                                     width=260,
                                                     text='Some Questions here!!', 
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, 'italic'))
        
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

       
        # correct tick ✅
        self.right_btn = Button(text="✅", font=(40), command=self.true_func)
        self.right_btn.config(highlightthickness=0, bg='green')
        self.right_btn.grid(row=2, column=0)
        # wrong tick button❌
        self.wrong_btn = Button(text="❌", font=(40), command=self.false_func)
        self.wrong_btn.config(highlightthickness=0, bg="red")
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_qn()
        



        self.window.mainloop()



    def get_next_qn(self):
        self.canvas.config(bg='white')
        q_test = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text= q_test)
    
    def true_func(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_func(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_qn)