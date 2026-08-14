import GuessingArt
# Get your own ascii art at https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false
import random

print(GuessingArt.logo)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty.  Type 'easy' or 'hard':  ").lower()
if difficulty == "easy":
    guesses = 10
elif difficulty == "hard":
    guesses = 5
else:
    print("Incorrect entry, please enter again")

hidden_number = random.randint(1,100)

done = False
while not done:
    print(f"You have {guesses} attempts remaining to guess the number")
    guess = int(input("Make a guess:  "))
    if guess > hidden_number:
        print("Too high\nGuess again.")
        guesses -= 1
    elif guess < hidden_number:
        print("Too low.\nGuess again.")
        guesses -= 1
    else:
        print("You guessed correct.\nYou win!")
        done = True
        continue

    if guesses == 0:
        print("You've run out of guesses.  Please play again")
        done = True
