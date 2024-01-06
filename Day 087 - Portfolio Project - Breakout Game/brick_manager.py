from brick import Brick
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class BrickManager:
    def __init__(self):
        self.brick_list = []
        self.create_wall()

    def create_wall(self):
        y_position = 280
        color_num = 0
        for y_position in range(280, 213, -22):
            for x_position in range(-380, 381, 82):
                brick = Brick(x_position, y_position, COLORS[color_num])
                self.brick_list.append(brick)

            color_num += 1

