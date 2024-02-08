from question_model import Question
from data import *
from quiz_brain import QuizBrain


def category():
    category = [question_data, movie_question, computer_question, gk_question, music_qn]
    print('''Category:
          Random Questions
          Movie Questions
          Computer Questions
          Qk Questions
          Music Questions
          ''')
    choice = input("Enter the Category of topics you want to take quiz(random/movie/computer/gk/music)")
    if choice.lower() =='random':
        return question_data
    elif choice.lower() =='movie':
        return movie_question
    elif choice.lower() =='computer':
        return computer_question
    elif choice.lower() =='gk':
        return gk_question
    else:
        return music_qn

question_bank = []
for question in category():
    myQuestion = question['question']
    myAnswer = question['answer']
    newQuestion = Question(myQuestion, myAnswer)
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have successfully completed the Quiz.")
print(f"You have scored {quiz.score}/{(quiz.questionNo)}")