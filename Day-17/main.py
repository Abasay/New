from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def mine():
    question_bank = []

    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))

    newQuiz = QuizBrain(question_bank)

    while newQuiz.still_has_questions():
        newQuiz.next_question()

    print(f"You've completed the quiz\nYour final score is {newQuiz.score}/{len(question_bank)}")

#mine()