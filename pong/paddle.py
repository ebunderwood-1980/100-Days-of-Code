from turtle import Turtle

UP = 90
DOWN = 270


class Paddle:
    def __init__(self, x_coord):
        self.paddle = []
        y_coord = 50
        for _ in range(5):
            piece = Turtle()
            piece.color("white")
            piece.shape("square")
            piece.penup()
            piece.setpos(x_coord, y_coord)
            self.paddle.append(piece)
            y_coord -= 20
            piece.setheading(DOWN)
        self.head = self.paddle[0]

    def move(self):
        for segment in self.paddle:
            segment.forward(20)

    def up(self):
        if self.head.heading() != UP:
            for segment in self.paddle:
                segment.setheading(UP)
        self.move()

    def down(self):
        if self.head.heading() != DOWN:
            for segment in self.paddle:
                segment.setheading(DOWN)
        self.move()
