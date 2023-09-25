# Import the Turtle class from the turtle module
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    # Constructor method for initializing a Paddle object
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Turtle)
        self.shape("square")  # Set the square shape
        self.color(random.choice(COLORS))  # Set the color randomly
        self.penup()  # Lift the pen to avoid drawing when moving
        self.goto(340, random.randint(-250, 250))  # Set the initial position of the car
        self.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the car's height (vertical size) by a factor of 1 and width (horizontal size) as 2

    def move(self, move_distance):
        self.setx(self.xcor() - move_distance)
