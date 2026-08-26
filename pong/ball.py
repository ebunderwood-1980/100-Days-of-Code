from turtle import Turtle


class Ball(Turtle):
    # Contructor
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("red")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    # Methods
    def move(self):
        xCoord = self.xcor() + self.xmove
        yCoord = self.ycor() + self.ymove
        self.goto(xCoord, yCoord)

    def bounceY(self):
        self.ymove *= -1

    def bounceX(self):
        self.xmove *= -1
