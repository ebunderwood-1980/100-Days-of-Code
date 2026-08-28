from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Arial", 14, "bold"),
        )
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Arial", 14, "bold"),
        )

    def print_final_score(self):
        self.home()
        self.write(
            "Game Over!",
            move=False,
            align="center",
            font=("Arial", 26, "bold"),
        )
