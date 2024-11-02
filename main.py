import requests, html
from ui import QuizInterface
response = requests.get(url='https://opentdb.com/api.php?amount=10&category=31&type=boolean')
response.raise_for_status()
question_data = response.json()['results']


from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


