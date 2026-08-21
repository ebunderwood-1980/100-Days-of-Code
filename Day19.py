# How to record keystrokes on Turtle
# Event Listeners
from turtle import Turtle, Screen


def move_foward():
    tim.forward(10)


tim = Turtle()
screen = Screen()


screen.listen()
screen.onkey(key="space", fun=move_foward)  #-- Executes move_forward() every time space is hit.

screen.exitonclick()


# Use functions as Inputs
def function_a(something):
    #Do this with something
    # Then Do this
    # Finally do this.

def function_b():
    # Do this

function_a(function_b)  #-- When you pass a function as an input, you do not include the parenthesis.

# Functions that work with other functions is called a Higher Order function.


