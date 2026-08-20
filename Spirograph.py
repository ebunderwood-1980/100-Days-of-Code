import turtle as t
from turtle import Screen
import random

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim = t.Turtle()
tim.shape("turtle")
tim.pen({
            "pensize": 2,
            "speed": 20,
        })
size_of_gap = int(input("Size of gap:  "))
for _ in range(int(360/size_of_gap)):
    tim.color(random_color())
    tim.circle(135)
    tim.right(size_of_gap)


screen = Screen()
screen.exitonclick()

