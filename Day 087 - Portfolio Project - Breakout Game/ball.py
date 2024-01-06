from turtle import Turtle
# Constants representing different directions
RIGHT_UP = 45
LEFT_UP = 135
LEFT_DOWN = 225
RIGHT_DOWN = 315


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # Set up the ball attributes
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.setheading(RIGHT_UP)
        self.move_speed = 0.05

    def move(self):
        # Move the ball forward by a fixed distance
        self.forward(10)

    def bounce_horizontal(self):
        # Change the heading of the ball when it hits a horizontal boundary
        current_heading = self.heading()
        if current_heading == RIGHT_UP:
            self.setheading(RIGHT_DOWN)
        elif current_heading == RIGHT_DOWN:
            self.setheading(RIGHT_UP)
        elif current_heading == LEFT_UP:
            self.setheading(LEFT_DOWN)
        else:
            self.setheading(LEFT_UP)

    def bounce_vertical(self):
        # Change the heading of the ball when it hits a vertical boundary
        current_heading = self.heading()
        if current_heading == RIGHT_UP:
            self.setheading(LEFT_UP)
        elif current_heading == RIGHT_DOWN:
            self.setheading(LEFT_DOWN)
        elif current_heading == LEFT_UP:
            self.setheading(RIGHT_UP)
        else:
            self.setheading(RIGHT_DOWN)

    def increase_speed(self):
        # Increase the speed of the ball
        self.move_speed = self.move_speed * 0.9

    def reset_game(self):
        # Reset the ball's position, speed, and heading
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_vertical()
