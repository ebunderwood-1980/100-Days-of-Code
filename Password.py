# Password Generator
import string
import random

letters = list(string.ascii_letters)
symbols = ["@", "#", "$", "%", "&", "*"]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Welcome to the password generator")
nr_letters = int(input("How many letters would you like in your password?  "))
nr_numbers = int(input("How many numbers would you like in your password?  "))
nr_symbols = int(input("How many symbols would you like in your password?  "))

password = []

for num in range(0, nr_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])


for num in range(0, nr_symbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])


for num in range(0, nr_numbers):
    password.append(digits[random.randint(0, len(digits) - 1)])

random.shuffle(password)
print(f"Here is your password: {password}")
