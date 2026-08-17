# Object Oriented Programming
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)


# Python Packages
# pypi.org has software packages developed by the community.

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

table.align = "l"

print(table)
