from turtle import Turtle
import constants


class Scoreboard(Turtle):
    # Constructor
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.computer_score = 0
        self.goto(0, constants.HEIGHT - 100)
        self.penup()
        self.color("white")
        self.write(
            f"User Score = {self.user_score}    Computer Score = {self.computer_score}",
            move=False,
            align="center",
            font=("Arial", 16, "bold"),
        )
