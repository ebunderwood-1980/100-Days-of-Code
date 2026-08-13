import BlackjackArt
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
done = False
userHand = []
computerHand = []

def userGameLoop(hand):
    stay = False
    while not stay:
        take_hit = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
        if take_hit == 'y':
            hand.append(random.choices(cards, k=1)[0])
            if sum(hand) > 21:
                return hand
            else:
                print(f"\tYour cards:  {hand}, current score:  {sum(hand)}")
                print(f"\tComputer's first card:  {computerHand[1]}")
        else:
            stay = True
    return hand

def computerGameLoop(hand):
    while sum(hand)<=17:
        hand.append(random.choices(cards, k=1)[0])
    
    return hand

while not done:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()
    if play == "n":
        done = True
        continue

    print(BlackjackArt.logo)

    userHand = random.choices(cards, k=2)
    computerHand = random.choices(cards, k=2)

    print(f"\tYour cards:  {userHand}, current score: {sum(userHand)}")

    if computerHand[1] >= 10 and (sum(computerHand) == 21):
        print(f"\tComputer's final hand:  {computerHand}")
        print("You loose, Computer has Blackjack")
        continue
    else:
        print(f"\tComputer's first card:  {computerHand[1]}")
        userHand = userGameLoop(userHand)
        computerHand = computerGameLoop(computerHand)

        print(f"\tYour final cards:  {userHand}, final score:  {sum(userHand)}")
        print(f"\tComputer's final hand:  {computerHand}, final score: {sum(computerHand)}")
        
       
    
