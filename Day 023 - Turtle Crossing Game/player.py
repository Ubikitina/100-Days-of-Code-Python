# Import the Turtle class from the turtle module
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Turtle)
        self.shape("turtle")
        self.color("black")  # Set the color
        self.setheading(90)
        self.penup()  # Lift the pen to avoid drawing when moving
        self.goto(STARTING_POSITION)  # Set the initial position of the paddle

    # Method to move the turtle up
    def up(self):
        # Increase the y-coordinate to move the paddle up by MOVE_DISTANCE pixels
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

