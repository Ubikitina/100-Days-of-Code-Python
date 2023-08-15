import turtle
import random

# Set up the screen and turtle
screen = turtle.Screen()
tim = turtle.Turtle()
tim.speed(0)  # This is the fastest speed

########### Challenge 5 - Spirograph ########
number_circles = 60
for i in range(number_circles):
    tim.color(random.random(), random.random(), random.random())
    # Draw a circle
    tim.circle(100)  # 100 is the radius of the circle
    tim.setheading(360*i/number_circles)

# Close the turtle graphics window when clicked
screen.exitonclick()