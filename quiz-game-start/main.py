import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from opentrivia import ClsOpenTrivia

request = ClsOpenTrivia()

# request.ask_category()

request.question_count()

# question_bank = []
# for question in data.question_data:
#     question_bank.append(Question(question['text'],question['answer']))
#
# qb = QuizBrain(question_bank)
# while qb.still_has_questions():
#     qb.next_question()
