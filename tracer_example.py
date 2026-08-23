import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 600)

# 1. TURN OFF ANIMATION
screen.tracer(0)

# Create the turtle
player = turtle.Turtle()
player.shape("square")
player.penup()

# Main game/animation loop
for _ in range(100):
    player.forward(2)  # Move in the background
    player.right(5)  # Rotate in the background

    # 2. MANUALLY REFRESH THE SCREEN
    screen.update()  # Renders the changes instantly

    time.sleep(0.02)  # Control the frame rate (fps)

screen.mainloop()


# The Core Concept

# screen.tracer(0): Turns off automatic, step-by-step drawing animations. The turtle still draws behind the scenes, but the result remains invisible to the user.

# screen.update(): Forces the screen to instantly refresh and display everything the turtle has drawn since the last update.

# By pairing these two methods, your script runs much faster because Python skips rendering thousands of individual intermediate drawing steps
