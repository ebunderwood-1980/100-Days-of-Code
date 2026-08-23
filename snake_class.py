from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # Initialize
    def __init__(self):
        self.snake = []
        x_coord = 0
        for _ in range(3):  # Creates individual parts of the snake
            new_piece = Turtle()
            new_piece.shape("square")
            new_piece.color("white")
            new_piece.penup()
            new_piece.goto(x_coord, 0)
            self.snake.append(new_piece)
            x_coord -= 20
        self.head = self.snake[0]

    # Methods
    def move(self):
        for segment_number in range((len(self.snake) - 1), 0, -1):
            new_x = self.snake[segment_number - 1].xcor()
            new_y = self.snake[segment_number - 1].ycor()
            self.snake[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
