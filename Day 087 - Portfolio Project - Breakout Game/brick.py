from turtle import Turtle

class Brick(Turtle):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()  # Call the constructor of the parent class (Turtle)
        self.shape("square")  # Set the square shape
        self.color(color)  # Set the color
        self.penup()  # Lift the pen to avoid drawing when moving
        self.goto(x_pos, y_pos)  # Set the position
        self.shapesize(stretch_wid=1, stretch_len=4)  # Stretch the height (vertical size) by a factor of 1 and width (horizontal size) as 2
