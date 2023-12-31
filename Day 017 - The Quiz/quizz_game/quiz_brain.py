class QuizBrain():
    def __init__(self, questions_list):
        self.question_number = 0 # Default value is 0 because all our quiz's will start with the first question.
                            # It will keep track on which question are we currently on.
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        # Will pull up a question from the list
        user_answer = input("Q." + str(self.question_number+1) +": " + self.questions_list[self.question_number].text + " (True/False)?: ")
        self.check_answer(user_answer, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print("The correct answer was: " + correct_answer + ".")
        print("Your current score is: {}/{}.".format(str(self.score), str(self.question_number+1)))
        print()

