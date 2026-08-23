# The game of snake.

from turtle import Screen
import random
import time
from snake_class import Snake

# Set up the game window.
game_window = Screen()
game_window.setup(width=600, height=600)
game_window.bgcolor("black")
game_window.title("My Snake Game")
game_window.tracer(0)  # -- Smooths out snake animation

# Set up our snake
snake = Snake()

# Set up snake movement
game_window.listen()
game_window.onkey(key="w", fun=snake.up)
game_window.onkey(key="a", fun=snake.left)
game_window.onkey(key="s", fun=snake.down)
game_window.onkey(key="d", fun=snake.right)


# Move the snake
game_is_on = True
while game_is_on:
    game_window.update()  # -- Smooths out snake animation
    time.sleep(0.1)
    snake.move()


game_window.exitonclick()
