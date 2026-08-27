from turtle import Screen
import time
from player_turtle import PlayerTurtle
from scoreboard import Scoreboard
from the_car import TheCar

# Create the "road" (screen)
road = Screen()
road.bgcolor("white")
road.setup(height=600, width=600)
road.title("Turtle Crossing")
road.tracer(0)

# Create the turtle
timmy = PlayerTurtle()

# Create a Car
my_car = TheCar()

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
cars = []
next_trigger = time.time() + 1.0

while still_playing:
    current_time = time.time()
    road.update()
    time.sleep(0.1)

    # Create a car
    if current_time >= next_trigger:
        new_car = TheCar()
        cars.append(new_car)
        next_trigger += 1.0

    # Get the cars moving
    for car in cars:
        car.move()

    # If Turtle crosses the road, increase level, start over.
    if timmy.ycor() >= 280:
        scoreboard.score()
        timmy.reset()

    # Check to see if turtle is ready for turtle soup.
    for car in cars:
        if timmy.distance(car) < 25:
            scoreboard.game_over()
            still_playing = False

# Keep the screen from disappearing
road.exitonclick()
