import turtle as t
from turtle import Screen
import random

COLORS = ["CadetBlue", "chartreuse", "chocolate", "CornflowerBlue", "DarkKhaki", "DarkSeaGreen4", "DarkSlateBlue", "DarkSlateGray", "DarkViolet", "DeepPink"]

DIRECTIONS = [0, 90, 180, 270, 360]

WALKLENGTH = 150
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =  (r,g,b)
    return random_color

tim = t.Turtle()
tim.shape("turtle")
tim.pen({
        "pensize": 15,
        "speed":20,
    }
)

for _ in range(WALKLENGTH):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(DIRECTIONS))    

screen = Screen()
screen.exitonclick()
