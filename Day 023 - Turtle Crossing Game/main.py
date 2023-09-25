import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player by using the Player class in player.py
player = Player()

# Create the car manager by using the CarManager class in car_manager.py
car_manager = CarManager()

# Create the scoreboard by using the Scoreboard class in scoreboard.py
scoreboard = Scoreboard()

# Listen to the keyboard only on determined keys and execute the corresponding paddle methods
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_all_cars()

    # Detect collision with car
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the turtle player has reached the top edge of the screen
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.level_up()


screen.exitonclick()
