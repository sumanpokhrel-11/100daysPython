class QuizBrain:
    def __init__(self, questionList):
        self.questionNo = 0
        self.questionList = questionList
        self.score = 0

   

    def next_question(self):
        currentQn = self.questionList[self.questionNo]
        self.questionNo += 1
        input(f"Q.{self.questionNo}: {currentQn.text} (True/False): ")


    def still_has_question(self):
        return self.questionNo < len(self.questionList)
    

    def next_question(self):
        currentQn = self.questionList[self.questionNo]
        self.questionNo += 1
        user_answer = input(f"Q.{self.questionNo}: {currentQn.text} (True/False): ")
        self.check_answer(user_answer, currentQn.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are correct")
            self.score +=1
        else:
            print("You are Wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current Score is: {self.score}/{self.questionNo}")






