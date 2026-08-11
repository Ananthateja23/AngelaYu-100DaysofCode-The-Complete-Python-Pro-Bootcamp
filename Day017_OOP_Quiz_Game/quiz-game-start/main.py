from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
"""
link of trivia database
1. https://opentdb.com/
2. paste the link on google
3. click on the API icon on homepage
4. select the number of questions, category, difficulty, and Type then hit the generate api button
5. copy the generated api link and paste again on a new tab
6. You get json formated questions, copy them and paste it in data.py
"""
question_bank = []
for question in question_data:
    # question_ob = Question(question['text'], question['answer'])
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

final_score = quiz.score
# total_question = len(question_bank)
final_question = quiz.question_number
print("You've completed the quiz")
print(f"Your final score was: {final_score}/{final_question}")