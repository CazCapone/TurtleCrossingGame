import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard


# Setup Screen
screen = Screen()
width, height = 600, 600
screen.setup(width, height)
screen.bgcolor("white")
screen.title("Crossing")
screen.tracer(0)

score = Scoreboard()
player = Player()
cars = Cars()

# Create movement controls
screen.listen()
screen.onkey(player.up, "Up")

# Game Loop
is_running = True

while is_running:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            is_running = False
    
    if player.is_at_finish():
        player.start_level()
        cars.level_up()
        score.next_level()

screen.exitonclick()