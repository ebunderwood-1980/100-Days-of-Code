# Create Money contants
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

WATER = 0
MILK = 1
COFFEE = 2
PRICE = 3

# Create Vending Machine Dictionary
vending_machine = {
    "Water": 1300,
    "Milk": 1200,
    "Coffee": 376,
    "Money": 0.00,
}

recipes_and_cost = {
    "espresso": [50, 0, 18, 1.50],
    "latte": [200, 24, 150, 2.50],
    "cappuccino": [250, 24, 100, 3.00],
}

transaction_complete = False


# Create 'report' functionality
def create_report():
    print(f"Water:  {vending_machine['Water']}ml")
    print(f"Milk:  {vending_machine['Milk']}ml")
    print(f"Coffee:  {vending_machine['Coffee']}ml")
    print(f"Money:  ${vending_machine['Money']:.2f}")


def resources_sufficient(user_choice):
    insufficient_list = ""
    if vending_machine["Water"] < recipes_and_cost[user_choice][WATER]:
        insufficient_list += "Water "
    if vending_machine["Milk"] < recipes_and_cost[user_choice][MILK]:
        insufficient_list += "Milk "
    if vending_machine["Coffee"] < recipes_and_cost[user_choice][COFFEE]:
        insufficient_list += "Coffee "

    if len(insufficient_list) == 0:
        return "True"
    else:
        return insufficient_list


def cash_paid(Q, D, N, P):
    total = (Q * QUARTERS) + (D * DIMES) + (N * NICKLES) + (P * PENNIES)
    return total


def transaction_successful(amount, drink):
    return amount >= recipes_and_cost[drink][PRICE]


def make_change(amount, drink):
    return amount - recipes_and_cost[drink][PRICE]


def update_vending(drink):
    vending_machine["Water"] -= recipes_and_cost[drink][WATER]
    vending_machine["Milk"] -= recipes_and_cost[drink][MILK]
    vending_machine["Coffee"] -= recipes_and_cost[drink][COFFEE]
    vending_machine["Money"] += recipes_and_cost[drink][PRICE]
    print(f"Here is your {drink}.")


# Check to see if resources are sufficient to make the drink in the vending machine
while not transaction_complete:
    # Ask user what they would like
    user_choice = input("What would you like?  (espresso/latte/cappuccino):  ").lower()
    if user_choice in ["espresso", "latte", "cappuccino"]:
        if resources_sufficient(user_choice) == "True":
            # Ask user to input coints and calculate how much money they have given you.
            print(
                f"Your total for your {user_choice} is ${recipes_and_cost[user_choice][PRICE]:.2f}."
            )
            quarters = int(input("How many quarters:  "))
            dimes = int(input("How many dimes:  "))
            nickles = int(input("How many nickles:  "))
            pennies = int(input("How many pennies:  "))
            amount_paid = cash_paid(quarters, dimes, nickles, pennies)
            print(f"You have paid:  ${amount_paid:.2f}.")
            if transaction_successful(amount_paid, user_choice):
                print(
                    f"Transaction successful, your change is ${make_change(amount_paid, user_choice):.2f}"
                )
                update_vending(user_choice)
            else:
                print("Need more cash, jackass")
                continue
        else:
            print(
                f"Not enough {resources_sufficient(user_choice)}to make {user_choice}."
            )
            continue
    elif user_choice == "done":
        transaction_complete = True
    elif user_choice == "report":
        create_report()
    else:
        print("Invalid command.  Please try again.")
        continue
