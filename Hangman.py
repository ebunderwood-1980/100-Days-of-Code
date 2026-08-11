import random
import WordList
import Stages


targetWord = random.choice(WordList.wordList)
targetList = []
lives = 6
gameOver = False
guessed = []

#print(f"The word is: {targetWord}")

for letter in range(len(targetWord)):
    targetList.append("_")
    

while not gameOver:
    userGuess = input("\nPlease guess a letter-->").lower()
    if userGuess in guessed:
        print(f"You have already guessed '{userGuess}'.  Please try again")
        continue
    else:
        guessed.append(userGuess)
        
    if userGuess in targetWord:
        for letter in range(len(targetWord)):
            if userGuess == targetWord[letter]:
                targetList[letter] = userGuess
    else:
        print("Incorrect Guess")
        lives -= 1
        print(Stages.stages[lives])

    print("".join(targetList))

    if targetWord == "".join(targetList):
        print("YOU WIN")
        gameOver = True
    elif lives == 0:
        print("YOU LOSE")
        print(f"The word you were looking for was '{targetWord}'")
        gameOver = True

    
    
