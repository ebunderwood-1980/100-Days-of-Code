from turtle import Turtle
import random


class TheCar(Turtle):
    # Constructor
    def __init__(self):
        super().__init__()
        color = ["red", "green", "blue", "gold", "orange", "purple"]
        self.shape("square")
        self.color(random.choice(color))
        self.shapesize(1, 2)
        self.penup()
        self.x_speed = 5
        starting_y = random.randint(-290, 290)
        self.goto(320, starting_y)

    # Methods
    def move(self):
        new_x = self.xcor() - self.x_speed
        self.goto(new_x, self.ycor())
