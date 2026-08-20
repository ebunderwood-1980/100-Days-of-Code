# Python Turtle Module
# Imported Python module that allows graphics to be drawn on the screen.

from turtle import Turtle
from turtle import Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DarkMagenta")

# for _ in range(4):   # -- Draws a square
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)  # -- Turns timmy right 90 degrees.

for _ in range(10):    #-- Draws a dashed line
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10) 
    


screen = Screen()
screen.exitonclick()


# Ways to import modules:
# import <module name>
# from <module name> import <Thing in Module>
# from <module name> import *     -- Imports everything from the module

# Aliasing modules:
# import <module name> as <alias> allows something like tim = t.Turtle()

# Installing modules:
# pip <module name>
# Then you can include <module name>



# Tuple
# my_tuple = (1,3,8)
# can access via square brackets.  my_tuple[2]
# You cannot move or change items in a tuple.  Called immutable.



