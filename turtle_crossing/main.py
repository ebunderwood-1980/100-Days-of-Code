from turtle import Screen
import time
from player_turtle import PlayerTurtle
from scoreboard import Scoreboard

# Create the "road" (screen)
road = Screen()
road.bgcolor("white")
road.setup(height=600, width=600)
road.title("Turtle Crossing")
road.tracer(0)

# Create the turtle
timmy = PlayerTurtle()

# Create the scoreboard
scoreboard = Scoreboard()

# Listens for movement keypresses to move turtle
road.listen()
road.onkey(key="w", fun=timmy.move_forward)
road.onkey(key="s", fun=timmy.move_backward)
road.onkey(key="a", fun=timmy.move_left)
road.onkey(key="d", fun=timmy.move_right)

# Allows me to quit from the keyboard
road.onkey(key="q", fun=road.bye)

# Game loop
still_playing = True

while still_playing:
    road.update()
    time.sleep(0.1)

    # If Turtle crosses the road, increase level, start over.
    if timmy.ycor() >= 280:
        scoreboard.score()
        timmy.reset()

# Keep the screen from disappearing
road.exitonclick()
