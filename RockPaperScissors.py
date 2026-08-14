import random

userChoice = int(
    input("What do you choose?  Type 0 for Rock, 1 for Paper, and 2 for Scissors. \n")
)
computerChoice = random.randint(0, 2)

if userChoice == 0:
    print("You chose Rock")
    if computerChoice == 0:
        print("Computer chose Rock")
        print("You tied.")
    elif computerChoice == 1:
        print("Computer chose Paper")
        print("You lost.")
    else:
        print("Computer chose Scissors")
        print("You win.")
elif userChoice == 1:
    print("You chose Paper")
    if computerChoice == 0:
        print("Computer chose Rock")
        print("You win.")
    elif computerChoice == 1:
        print("Computer chose Paper")
        print("You tied.")
    else:
        print("Computer chose Scissors")
        print("You lost.")
elif userChoice == 2:
    print("You chose Scissors")
    if computerChoice == 0:
        print("Computer chose Rock")
        print("You lost.")
    elif computerChoice == 1:
        print("Computer chose Paper")
        print("You win.")
    else:
        print("Computer chose Scissors")
        print("You tied.")
else:
    print("Invalid entry.  Go eat a dick")
