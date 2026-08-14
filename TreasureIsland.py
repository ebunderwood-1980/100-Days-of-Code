print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")

direction = input(
    "You are at a crossroad. Where do you want to go?  Type 'left' or 'right':  "
)
if direction != "right":
    print("You've come to a lake.  There is an island in the middle of the lake.")
    swim = input("     Type 'wait'to wait for the boat.  Type 'swim' to swim across.  ")
    if swim != "swim":
        print("You arrive at the island unharmed.  There is a house with three doors.")
        door = input(
            "     One red, one yellow, and one blue.  Which color do you choose?  "
        )
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by a fire.  Game over")
        elif door == "blue":
            print("Eaten by beasts.  Game over.")
        else:
            print("Game Over.")
    else:
        print("You are attacked by a trout.  Game over.")
else:
    print("You fall into a hole.  Game over.")
