i = int(input("Enter a number:  "))

if i % 2 == 0:
    print(f"{i} is Even")
else:
    print(f"{i} is Odd")

weight = 85
height = 1.85

bmi = weight / (height**2)


if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?  S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza?  Y or N:  ")
extraCheese = input("Do you want extra cheese?  Y or N:  ")
total = 0.00

if size == "S":
    total = 15
    if pepperoni == "Y":
        total += 2
elif size == "M":
    total = 20
    if pepperoni == "Y":
        total += 3
else:
    total = 25
    if pepperoni == "Y":
        total += 3

if extraCheese == "Y":
    total += 1

print(f"Your total is ${total:.2f}")
