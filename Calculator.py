import CalcArt

print(CalcArt.logo)

done = False
start_over = True

def calculate(n1, n2, operator):
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        return n1 / n2
    else:
        return "Error"

while not done:
    if start_over:
        first_number = float(input("What's the first number?:  "))
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Pick an operation:  ")
    second_number = float(input("What's the second number?:  "))
    result = calculate(first_number, second_number, operation)

    print(f"{first_number} {operation} {second_number} = {result}\n")

    resume = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation:  ")

    if resume == "y":
        first_number = result
        start_over = False
    elif resume == "q":
        done = True
    else:
        start_over = True
        

    
    
