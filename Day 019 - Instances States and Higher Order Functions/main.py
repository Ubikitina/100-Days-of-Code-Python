"""
Turtle Race

This script creates a turtle race simulation using the Turtle graphics library.

Author: Ubikitina

"""

from turtle import Turtle, Screen
import random


def create_turtle():
    """
    Create a turtle with a unique color from the color list.

    Returns:
    Turtle: A turtle object with a specified shape and color.
    """
    global color_number
    # Create a turtle
    tim = Turtle(shape="turtle")
    tim.color(color_list[color_number])
    color_number += 1
    tim.penup()
    return tim


# Set up the screen
screen = Screen()
screen.setup(500, 400)  # Setup the dimensions of the screen

# Get user's bet on the winning turtle's color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of colors and initial turtle position
color_list  = ["red", "orange", "yellow", "green", "blue", "pink", "purple", "brown"]
x_position = -230
y_position = -175

# Initialize variables for color selection and random steps
color_number = 0
random_step_list = [1, 2, 10, 5]

# List to store turtle objects
list_of_turtles = []

# Loop to create and position the turtles
for _ in range(8):
    tur = create_turtle()  # Create a turtle
    tur.goto(x_position, y_position)  # Position the turtle
    y_position += 50  # Move the y_position for the next turtle
    list_of_turtles.append(tur)  # Add turtle to the list

continue_race = True
winner = ""

# Main race loop
while continue_race:
    # Move each turtle by a random step
    for turtle in list_of_turtles:
        turtle.forward(random.choice(random_step_list))

    # Check if any turtle has reached the finish line
    for turtle in list_of_turtles:
        if turtle.xcor() >= 230:
            continue_race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You've won! The " + winner + " turtle is the winner!")
            else:
                print("You've lost! The " + winner + " turtle is the winner!")

# Close the screen on click
screen.exitonclick()
