from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick_manager import BrickManager
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)  # Turn off the animation updates. Then we will use screen.update() to display the accumulated changes all at once

# Create the paddle by using the Paddle class in paddle.py file
paddle = Paddle(0, -250)

# Create the ball by using the Ball class in ball.py
ball = Ball()

# Create the brick manager
brickmanager = BrickManager()

# Create the scoreboard by using the Scoreboard class in scoreboard.py
scoreboard = Scoreboard()

# Listen to the keyboard only on determined keys and execute the corresponding paddle methods
screen.listen()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280:  # Top wall
        ball.bounce_horizontal()
    elif ball.xcor() > 380 or ball.xcor() < -380:  # Right wall or left wall
        ball.bounce_vertical()

    # Detect collision with the paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_horizontal()
        ball.increase_speed()  # Increase the speed of the ball

    # Detect if the ball goes out of bounds at the botton of the screen without colliding with the paddle
    elif ball.ycor() < -281:
        ball.reset_game()
        paddle.goto(0, -250)
        scoreboard.decrease_lives()

    # Detect collision with the brick
    for brick in brickmanager.brick_list:
        if brick.distance(ball) < 30:
            ball.bounce_horizontal()
            brick.goto(500,0) # go to a non visible position
            brickmanager.brick_list.remove(brick) # remove the brick from the list

    if scoreboard.score_lives == 0:
        game_is_on = False
        scoreboard.game_over()

    if not brickmanager.brick_list:
        game_is_on = False
        scoreboard.you_win()

screen.exitonclick()
