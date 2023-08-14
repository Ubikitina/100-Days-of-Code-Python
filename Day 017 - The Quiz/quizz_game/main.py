from question_model import Question
from data import question_data, other_questions
from quiz_brain import QuizBrain

question_bank = []
for entry in other_questions:
    question_object = Question(entry["question"], entry["correct_answer"])
    question_bank.append(question_object)

my_quiz_brain = QuizBrain(question_bank)
while my_quiz_brain.still_has_questions():
    my_quiz_brain.next_question()

print("You've completed the quiz.")
print("Your final score was {}/{}.".format(str(my_quiz_brain.score), str(my_quiz_brain.question_number)))
