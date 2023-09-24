from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# tracer() is used to control the animation speed of the drawings created using the turtle graphics module.
# The parameter passed to this method determines how many screen updates (or frames) are skipped
# before actually updating the display. In this case, passing 0 as the parameter means that the animation updates are
# turned off or suppressed.
# When the animation updates are turned off using screen.tracer(0), any drawings or operations performed using the
# Turtle module won't be immediately displayed on the screen. Instead, they will be cached in memory without causing
# visual updates. Then use screen.update() to display the accumulated changes all at once when you're ready.
screen.tracer(0)

# Create the paddles by using the Paddle class in paddle.py file
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Create the ball by using the Ball class in ball.py
ball = Ball()

# Create the scoreboard by using the Scoreboard class in scoreboard.py
scoreboard = Scoreboard()

# Listen to the keyboard only on determined keys and execute the corresponding paddle methods
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_horizontal()

    # Detect collision with a paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_vertical()
        ball.increase_speed()  # Increase the speed of the ball

    # Detect if the ball goes out of bounds at the edge of the screen for the right player
    if ball.xcor() > 380:
        ball.reset_game()
        scoreboard.increase_score_left()

    # Detect if the ball goes out of bounds at the edge of the screen for the left player
    elif ball.xcor() < -380:
        ball.reset_game()
        scoreboard.increase_score_right()


screen.exitonclick()
