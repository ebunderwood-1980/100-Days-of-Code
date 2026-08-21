from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)

user_winner_choice = screen.textinput(title="Select a Winner", prompt="Which tutrle will win the race?  Pick a color:").lower()

racers = []
x_pos = -237
y_pos = -150

for color in COLORS:
    random_turtle = Turtle(shape = "turtle")
    random_turtle.color(color)
    random_turtle.penup()
    random_turtle.goto(x=x_pos, y=y_pos)
    racers.append(random_turtle)
    y_pos += 60

over = False
winning_color = ""
while not over:
    for racer in racers:
        racer.forward(random.randint(1,10))
        if racer.xcor() >= 237:
            winning_color = racer.color()
            over = True

if user_winner_choice == winning_color[0]:
    print("You are the winner.  Nice job!")
else:
    print(f"You loose!  {winning_color[0].title()} was the winner.")
        
        
screen.exitonclick()
