from data import question_data
from question_model import Question

class QuizBrain:

    def __init__(self, queList):
        self.question_number = 0
        self.questions_list = queList

    def askQuestion(self):
        print(f"Q{self.question_number+1}. {self.questions_list[self.question_number].question}")
        tof = input("True or False: ")

        if tof == self.questions_list[self.question_number].answer:
            self.question_number += 1
            return True
        else:
            return False

    def queRemaining(self):
        if self.question_number == len(self.questions_list):
            return False

        else:
            return True

    def returnAnswer(self):
        return self.questions_list[self.question_number].answer