import GameData
import HigherLowerArt as art
import random
import os


def printLogo():
    print(art.logo)


def getPerson():
    return random.choice(GameData.data)


def moreFollowers(person_a, person_b):
    if person_a["follower_count"] > person_b["follower_count"]:
        return "a"
    else:
        return "b"


score = 0
gameOver = False

# Step 1:  Print Higher/Lower logo
printLogo()
person_one = getPerson()

# Step 2:  Pick out two random peope from the dictionary, formatted NAME, DISCRIPTION, WHERE FROM.
while not gameOver:
    person_two = getPerson()
    while person_one == person_two:
        person_two = getPerson()

    os.system("cls")
    printLogo()
    if score > 0:
        print(f"You're right!  Current score:  {score}")

    print(
        f"Compare A:  {person_one['name']}, {person_one['description']}, from {person_one['country']}"
    )
    print(art.vs)
    print(
        f"Against B:  {person_two['name']}, {person_two['description']}, from {person_two['country']}"
    )

    # Step 3:  Ask for user to pick who they think has more followers.
    guess = input("Who has more followers?  Type 'A' or 'B':  ").lower()

    # Step 4:  If user choice is correct, move choice to first people, increment number correct, and pick a random 2nd person
    #         If user choice is incorrect, tell them they lost, print out their score, and end game.
    if (guess == "a" and moreFollowers(person_one, person_two) == "a") or (
        guess == "b" and moreFollowers(person_one, person_two) == "b"
    ):
        score += 1
        if guess == "b":
            person_one = person_two
    else:
        print(f"Sorry, that's wrong.  Final score:  {score}")
        gameOver = True
