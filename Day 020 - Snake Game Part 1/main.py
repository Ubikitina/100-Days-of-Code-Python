from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# tracer() is used to control the animation speed of the drawings created using the turtle graphics module.
# The parameter passed to this method determines how many screen updates (or frames) are skipped
# before actually updating the display. In this case, passing 0 as the parameter means that the animation updates are
# turned off or suppressed.
# When the animation updates are turned off using screen.tracer(0), any drawings or operations performed using the
# Turtle module won't be immediately displayed on the screen. Instead, they will be cached in memory without causing
# visual updates. Then use screen.update() to display the accumulated changes all at once when you're ready.
screen.tracer(0)

# Create the snake by using the Snake class in snake.py file
snake = Snake()

# Listen to the keyboard only on determined keys and execute the corresponding snake methods
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
