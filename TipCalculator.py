print("Welcome to the tip calculator")
totalBill = input("What was the total bill?  $")
tip = input("How much tip would you like to give?  10, 12, or 15?  ")
people = input("How many people to split the bill?  ")

answer = float(totalBill) + (float(totalBill) * (float(tip)/100))
amountOwed = round(answer/int(people), 2)
print(f"Each person should pay ${amountOwed}")

