import turtle
import random


def draw_line():
    for _ in range(10):  # Draw 10 dots per line
        tim.pencolor(random.choice(rgb_colors))
        tim.dot(20)  # Dot size is 20
        tim.forward(50)  # Space between dots is 50


rgb_colors = [(249, 248, 248), (237, 241, 245), (238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17),
              (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24),
              (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163),
              (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147),
              (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]

# Set up the screen and turtle
screen = turtle.Screen()
screen.colormode(255)
tim = turtle.Turtle()
tim.speed(0)  # This is the fastest speed
tim.penup()
tim.hideturtle()

# Set the drawing position using the goto() function
x_position = -250
y_position = -200

for _ in range(10):
    tim.goto(x_position, y_position)  # Go to the starting position of each line
    draw_line()
    y_position += 50  # The drawing should be done from top bottom to top, distance between lines is 50

# Close the turtle graphics window when clicked
screen.exitonclick()
