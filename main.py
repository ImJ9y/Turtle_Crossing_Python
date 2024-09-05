import time
from turtle import Screen
from Player import Player
from car_manager import CarManager
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreBoard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # when turtle reached goal
    if player.at_finish_line():
        player.reset()
        scoreBoard.player_point()
        cars.MOVE_INCREMENT()

screen.exitonclick()