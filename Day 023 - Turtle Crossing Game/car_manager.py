from car import Car
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Car()
            self.car_list.append(car)

    def move_all_cars(self):
        for car in self.car_list:
            car.move(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


