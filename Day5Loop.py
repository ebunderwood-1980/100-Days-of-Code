fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

scores = [180, 142, 285, 120, 171, 184]
max = 0

for score in scores:
    if score > max:
        max = score

print(f"The max number in the list is {max}")

# Range function for loops
total = 0
for number in range(1, 101):
    total += number

print(f"The total is {total}")

# FizzBuzz and whatnot.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
