import Player
from Player import *
from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
ALIGMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 250)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.player_level}", align=ALIGMENT, font=FONT)

    def player_point(self):
        self.player_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGMENT, font=FONT)
