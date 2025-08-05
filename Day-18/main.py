from data import question_data
from question_model import Question
from quiz_brain import Quiz
question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))


quiz = Quiz(question_bank)

while quiz.still_active():
    quiz.next_question()

print(f"You got {quiz.score} out of {len(question_bank)}")