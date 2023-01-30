from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand = random.randint(1, 6)
        if rand == 1:
            new = Turtle("square")
            new.shapesize(stretch_len=2, stretch_wid=1)
            new.penup()
            new.color(random.choice(COLORS))
            #new.setheading(180)
            rand_y = random.randint(-250, 250)
            new.goto(300, rand_y)
            self.all_cars.append(new)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT