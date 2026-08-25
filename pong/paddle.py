from turtle import Turtle
import constants as C


class Paddle(Turtle):
    # Constructor
    def __init__(self, xCoord):
        super().__init__()
        self.paddle = []
        y_coord = 40
        for _ in range(C.PADDLESIZE):
            part = Turtle()
            part.color("white")
            part.shape("square")
            part.penup()
            part.goto(xCoord, y_coord)
            part.setheading(90)
            self.paddle.append(part)
            y_coord -= 20

    def move_up(self):
        print("Moveing Up")
        for part in self.paddle:
            if part.heading() != 90:
                part.setheading(90)
                part.forward(20)

    def move_down(self):
        print("Moving Down")
        for part in self.paddle:
            if part.heading() != 270:
                part.setheading(270)
                part.forward(20)
