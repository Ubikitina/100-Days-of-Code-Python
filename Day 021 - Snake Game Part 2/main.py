from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

# Create the food by using the Food class in food.py
food = Food()

# Create the scoreboard by using the Scoreboard class in scoreboard.py
scoreboard = Scoreboard()

# Listen to the keyboard only on determined keys and execute the corresponding snake methods
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if head collides with any segment in the tail
    for segment in snake.body_of_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
