from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []

for i in range(len(question_data)):
    questionBank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(questionBank)



still_has_question = True

correctAns = True

while still_has_question and correctAns:
    correctAns = quiz.askQuestion()
    if correctAns == False:
        print(f"Wrong! The correct answer was {quiz.returnAnswer()}")
    still_has_question = quiz.queRemaining()

    if still_has_question == False:
        print("You answered all questions correctly! You Win!")