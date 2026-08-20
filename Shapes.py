from turtle import Turtle as T
from turtle import Screen as S
import random

def draw(sides, new_color):
    tim.pencolor(new_color)
    turn_angle = 360 / sides
    for _ in range(sides):
        tim.right(turn_angle)
        tim.forward(100)
        
tim = T()
tim.shape("turtle")
colors = ["red", "green", "blue", "indianred", "firebrick", "ForestGreen", "skyblue", "gold", "magenta"]

for sides in range (3,11):
    draw(sides, random.choice(colors))


screen = S()
screen.exitonclick()


