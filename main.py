from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_q = Question(question_text,question_answer)
    question_bank.append(new_q)


quiz = Quiz_brain(question_bank)
while quiz.still_have_question():
    quiz.next_question()
    

