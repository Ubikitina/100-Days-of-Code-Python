import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

########### Challenge 3 - Draw Shapes ########
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for num_sides in range(3, 11):
    tim.color(random.random(), random.random(), random.random())
    draw_shape(num_sides)

# Create a turtle screen named 'my_screen'
my_screen = t.Screen()
# Wait for a click on the screen and then close it
my_screen.exitonclick()