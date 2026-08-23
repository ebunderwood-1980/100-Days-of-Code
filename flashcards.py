flashcards = {
    "one": 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
}

def print_menu():
    '''Prints the main menu and get an input'''
    print("What would you like to do:")
    print("\t1. Take quiz.")
    print("\t2. Add flashard.")
    print("\t3. Delete flashard.")
    print("\t4. Exit.")
    return(int(input("Enter 1-4:  ")))

def add_card():
    key = input("Enter the question:  ").lower()
    answer = int(input("Enter the answer:  "))
    flashcards[key] = answer
    print("...Card Added.")

def delete_card():
    card_list = ""
    for card in flashcards:
        card_list += f"{card}, "
    print(f"Cards available:  {card_list}")
    user_choice = input("What would you like to delete?:  ").lower()
    flashcards.pop(user_choice, None)
    print("...Card Deleted.")


def take_quiz():
    for card in flashcards:
        user_input = int(input(f" {card}:  "))
        if user_input == flashcards[card]:
            print("Correct.")
        else:
            print("Incorrect.")

# Program Loop
done = False

while not done:

    # Gather user info
    user_input = print_menu()

    match user_input:
        case 1:
            print("Taking a quiz")
            take_quiz()
        case 2:
            print("Adding a Flashcard")
            add_card()
            print(flashcards)
        case 3:
            print("Deleting a flashcard")
            delete_card()
        case 4:
            print("Exiting")
            done = True
        case _:
            print("Invalid input.  Please try again.")
    
