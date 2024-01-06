# Import the Turtle class from the turtle module
from turtle import Turtle

# Define a constant for the distance the paddle moves in each step
MOVE_DISTANCE = 20


# Create a class called Paddle that inherits from Turtle
class Paddle(Turtle):
    # Constructor method for initializing a Paddle object
    def __init__(self, x_position, y_position):
        super().__init__()  # Call the constructor of the parent class (Turtle)
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.penup()  # Lift the pen to avoid drawing when moving
        self.goto(x_position, y_position)  # Set the initial position of the paddle
        self.shapesize(stretch_wid=1, stretch_len=5)  # Stretch the paddle's height (vertical size) by a factor of 5 and keep the width (horizontal size) as 1

    # Method to move the paddle to the right
    def right(self):
        # Increase the x-coordinate to move the paddle to the right by MOVE_DISTANCE pixels
        self.setx(self.xcor() + MOVE_DISTANCE)

    # Method to move the paddle down
    def left(self):
        # Decrease the x-coordinate to move the paddle to the left by MOVE_DISTANCE pixels
        self.setx(self.xcor() - MOVE_DISTANCE)
