import BlackjackArt
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
done = False
userHand = []
computerHand = []

while not done:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()
    if play == "n":
        done = True
        continue

    print(BlackjackArt.logo)

    userHand = random.choices(cards, k=2)
    computerHand = random.choices(cards, k=2)

    print(f"Your cards:  {userHand}, current score: {sum(userHand)}")
    print(f"Computer's first card:  {computerHand[1]}")

    if computerHand[1] >= 10 and (computerHand[0] + computerHand[1] == 21):
        print("Lose, opponent has Blackjack")
        continue

    takeHit = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
    while takeHit == 'y':
        userHand.append(random.choice(cards))
        print(f"Your cards:  {userHand}, current score: {sum(userHand)}")
        if sum(userHand) > 21:
            

       
    
