from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    quiz_question = Question(question=question['text'], answer=question['answer'])
    question_bank.append(quiz_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
