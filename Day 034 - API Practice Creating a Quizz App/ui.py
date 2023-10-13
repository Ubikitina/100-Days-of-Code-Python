from tkinter import *
from quiz_brain import QuizBrain  # Import the QuizBrain class from quiz_brain module

THEME_COLOR = "#375362"  # Set the THEME_COLOR variable to a specific color code

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        """
        Initialize the QuizInterface.

        Args:
            quiz_brain (QuizBrain): The QuizBrain object that manages the quiz questions.

        This method sets up the user interface for the quiz application.
        """

        # Initialize the QuizInterface with a QuizBrain object
        self.quiz = quiz_brain

        # Create a Tkinter window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # Configure window padding and background color

        # Create the score label
        self.score_label = Label(text=f"Score: 0", font=("Arial", 10), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)  # Use the grid geometry manager

        # Create a canvas widget for drawing graphics
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quizz_text = self.canvas.create_text(150, 125, width=280, text="Placeholder for the question", fill="black", font=("Arial", 20, "italic"))  # Create a text element on the canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # Use the grid geometry manager to position the canvas in the window

        # Load the image
        true_image = PhotoImage(file="images/true.png")
        # Create the True button
        self.true_button = Button(image=true_image, command=self.true_button_pressed, highlightthickness=0)
        self.true_button.grid(row=2, column=0)  # Use the grid geometry manager

        # Load the image
        false_image = PhotoImage(file="images/false.png")
        # Create the False button
        self.false_button = Button(image=false_image, command=self.false_button_pressed, highlightthickness=0)
        self.false_button.grid(row=2, column=1)  # Use the grid geometry manager

        self.get_next_question() # initialize with the first question

        # Start the Tkinter main loop
        self.window.mainloop()

    def get_next_question(self):
        """
        Get and display the next quiz question.

        This method retrieves the next question from the QuizBrain object and updates the interface to display it.
        If there are no more questions, it displays an end-of-quiz message.
        """

        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quizz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quizz_text, text="You've reached the end of the quiz")
            # Disable true and false buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        """
        Handle the "True" button click.

        This method is called when the "True" button is clicked. It checks the user's answer and provides feedback.
        """

        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_pressed(self):
        """
        Handle the "False" button click.

        This method is called when the "False" button is clicked. It checks the user's answer and provides feedback.
        """

        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """
        Provide feedback to the user.

        Args:
            is_right (bool): Indicates whether the user's answer is correct.

        This method updates the background color of the canvas to provide visual feedback to the user.
        It schedules the next question to be displayed after a delay.
        """

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
