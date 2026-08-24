from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from paddle import Paddle
from pongball import Ball

# Set up the game window
game_window = Screen()
game_window.setup(width=600, height=600)
game_window.bgcolor("black")
game_window.title("My Game of Pong")

# Set up the score board
scoreboard = Scoreboard()

# Set up the ball
game_ball = Ball()

# Set up the user paddle on the left hand side and the computer paddle on the right hand side.  Set up the net in the middle of the screen.
game_window.tracer(0)
user_paddle = Paddle(x_coord=-280)
computer_paddle = Paddle(x_coord=280)

net = Turtle()
net.color("white")
net.penup()
net.goto(0, 260)
net.right(90)
while net.ycor() > -280:
    net.pendown()
    net.forward(30)
    net.penup()
    net.forward(30)
net.hideturtle()
game_window.update()

# Allow the paddle to move
game_window.listen()
game_window.onkey(key="w", fun=user_paddle.up)
game_window.onkey(key="s", fun=user_paddle.down)

# Game Loop
game_over = False
game_window.tracer(0)

while not game_over:
    game_window.update()
    time.sleep(0.01)
    game_ball.move()

    # Ball top wall logic
    if game_ball.ball.ycor() >= 280 or game_ball.ball.ycor() <= -280:
        game_ball.ball.setheading(game_ball.ball.heading() * -1)

    # Ball scoring logic
    if game_ball.ball.xcor() >= 280:
        ball_y_coord = game_ball.ball.ycor()
        for segment in user_paddle.paddle:
            if segment.ycor() == ball_y_coord:
                game_ball.ball.setheading(game_ball.ball.heading() * -1)
                break
        scoreboard.update_score("u")
        game_ball.reset()
    if game_ball.ball.xcor() <= -280:
        scoreboard.update_score("c")
        game_ball.reset()


# Exit game
game_window.exitonclick()
