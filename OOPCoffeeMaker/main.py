from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
cash_machine = MoneyMachine()
done = False

while not done:
# 1. Prompt user by asking what would you like.
    user_choice = input(f"What would you like?  ({menu.get_items()}):  ").lower()
    if user_choice == "off":
        done = True
        continue
    elif user_choice == "report":
        coffee_machine.report()
        cash_machine.report()
        continue
    else:
        drink = menu.find_drink(user_choice)
        if drink == None:
            print(f"I'm sorry, we do not have a {user_choice}, please select again.")
            continue
        else:
            if coffee_machine.is_resource_sufficient(drink):
                if(cash_machine.make_payment(drink.cost)):  
                    coffee_machine.make_coffee(drink)
                
            else:
                # coffee_machine.is_resource_sufficient() should print out error message before we continue.
                continue

