from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-270, 270)
        self.point = 1
        self.write(
            arg=f"Level:  {self.point}",
            align="left",
            font=("Courier", 14, "bold"),
        )
        self.hideturtle()

    # Methods
    def score(self):
        self.clear()
        self.point += 1
        self.write(
            arg=f"Level:  {self.point}",
            align="left",
            font=("Courier", 14, "bold"),
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg="GAME OVER!",
            align="center",
            font=("Courier", 26, "bold"),
        )
