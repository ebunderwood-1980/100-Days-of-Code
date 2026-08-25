from turtle import Screen
import constants as C
from paddle import Paddle

# Create the Screen
pong_table = Screen()
pong_table.bgcolor("black")
pong_table.setup(height=C.HEIGHT, width=C.WIDTH)
pong_table.title("PONG!")

# Create paddles that move
pong_table.tracer(0)
user_paddle = Paddle(-350)
computer_paddle = Paddle(350)
pong_table.update()


# Keep the screen from disappearing
pong_table.exitonclick()
