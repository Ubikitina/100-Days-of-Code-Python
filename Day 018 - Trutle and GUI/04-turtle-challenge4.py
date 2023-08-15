import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.speed(0)  # This is the fastest speed
tim.pensize(15)


def random_step():
    random_angle = 90 * random.randint(0,3)
    tim.color(random.random(), random.random(), random.random())
    tim.right(random_angle)
    tim.forward(25)

for _ in range(300):
    random_step()

# Create a turtle screen named 'my_screen'
my_screen = t.Screen()
# Wait for a click on the screen and then close it
my_screen.exitonclick()

