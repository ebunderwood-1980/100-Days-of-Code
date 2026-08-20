import turtle as t
from turtle import Screen
import colorgram
import random

t.colormode(255)

color_list = [(240, 245, 250), (234, 225, 84), (195, 8, 69), (231, 54, 132), (197, 77, 17), (113, 177, 213), (194, 164, 14), (216, 162, 102), (29, 104, 167), (34, 187, 113), (14, 24, 64), (20, 29, 169), (231, 224, 7), (215, 134, 177), (201, 32, 132), (14, 182, 210), (231, 167, 197)]

pen = t.Turtle()
pen.shape("circle")
pen.pen({
            "pensize":.5,
            "speed": 20,
        })

pen.hideturtle()

x_pos = -200
y_pos = -200

# Move the turtle to the starting postion
pen.penup()
pen.goto(x_pos,y_pos)
pen.pendown()

for row in range (10):
    for _ in range (10):
        pen.dot(30, random.choice(color_list))
        pen.penup()
        pen.forward(30)
        pen.pendown()
    pen.penup()
    y_pos += 40
    pen.goto(x_pos, y_pos)
    pen.pendown()


screen = Screen()
screen.exitonclick()
