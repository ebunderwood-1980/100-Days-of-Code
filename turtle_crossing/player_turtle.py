from turtle import Turtle


class PlayerTurtle(Turtle):
    # Constructor
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -270)
        self.setheading(90)

    def move_forward(self):
        xPos = self.xcor()
        yPos = self.ycor()
        if yPos < 280:
            self.goto(xPos, yPos + 10)

    def move_backward(self):
        xPos = self.xcor()
        yPos = self.ycor()
        if yPos > -280:
            self.goto(xPos, yPos - 10)

    def move_left(self):
        xPos = self.xcor()
        yPos = self.ycor()
        if xPos > -280:
            self.goto(xPos - 10, yPos)

    def move_right(self):
        xPos = self.xcor()
        yPos = self.ycor()
        if xPos < 280:
            self.goto(xPos + 10, yPos)

    def reset(self):
        self.goto(0, -270)
