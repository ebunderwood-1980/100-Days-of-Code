from turtle import Turtle
import random

SPEED = 4


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.turtlesize(1.5, 1.5, 1)
        self.ball.right(random.randint(-225, 135))
        self.ball.penup()

    def move(self):
        self.ball.forward(SPEED)

    def reset(self):
        self.ball.goto(0, 0)
