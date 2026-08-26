from turtle import Screen
import constants as C
from paddle import Paddle
from ball import Ball
import time

# Create the Screen
pong_table = Screen()
pong_table.bgcolor("black")
pong_table.setup(height=C.HEIGHT, width=C.WIDTH)
pong_table.title("PONG!")
pong_table.tracer(0)

# Create paddles that move
user_paddle = Paddle(-350)
computer_paddle = Paddle(350)

# Create the game ball
ball = Ball()

# Listens for movement key presses for both paddles.
pong_table.listen()
pong_table.onkey(key="r", fun=user_paddle.move_up)
pong_table.onkey(key="f", fun=user_paddle.move_down)
pong_table.onkey(key="u", fun=computer_paddle.move_up)
pong_table.onkey(key="j", fun=computer_paddle.move_down)

# Allows me to quit from the keyboard
pong_table.onkey(key="q", fun=pong_table.bye)

done = False

while not done:
    pong_table.update()
    time.sleep(0.1)

    ball.move()

    # Detect ball collion with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Detect ball collision with the paddle
    if ball.distance(computer_paddle) < 50 and ball.xcor() > 320:
        ball.bounceX()
    if ball.distance(user_paddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # Detect scoring events
    if ball.xcor() > 380:
        ball.new_point()
    if ball.xcor() < -380:
        ball.new_point()


# Keep the screen from disappearing
pong_table.exitonclick()
