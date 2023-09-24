from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.body_of_snake = []

        # Loop to create and position the turtles
        for _ in range(5):
            segment = self.create_snake_dot()  # Create a turtle
            segment.goto(self.x_position, self.y_position)  # Position the turtle
            self.x_position -= MOVE_DISTANCE  # Move the y_position for the next turtle
            self.body_of_snake.append(segment)  # Add turtle to the list



    # Create each of the dots on the snake body
    def create_snake_dot(self):
        global color_number
        dot = Turtle(shape="square")
        dot.color("white")
        dot.penup()
        return dot

    def folow_next_segment(self):
        for i in range(len(self.body_of_snake) - 1, 0, -1):
            x,y = self.body_of_snake[i-1].pos()
            print(f"Segment i-1 = {i-1} current position: x = {x}, y = {y}, assigned to segment i = {i}")
            self.body_of_snake[i].goto(x,y)

    def move(self):
        self.folow_next_segment()
        self.body_of_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        # Only allow to go up if the snake is not going down
        if self.body_of_snake[0].heading() != DOWN:
            self.body_of_snake[0].setheading(UP)

    def right(self):
        if self.body_of_snake[0].heading() != LEFT:
            self.body_of_snake[0].setheading(RIGHT)

    def down(self):
        if self.body_of_snake[0].heading() != UP:
            self.body_of_snake[0].setheading(DOWN)

    def left(self):
        if self.body_of_snake[0].heading() != RIGHT:
            self.body_of_snake[0].setheading(LEFT)