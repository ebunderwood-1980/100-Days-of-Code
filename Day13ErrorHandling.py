# Error Handling:  Try block

try:
    age = int(input("How old are you?  "))  # Try this
except ValueError:  # If you get an error message, do this.
    print("You have typed in an invalid number.  Please try again")
    age = int(input("How old are you?  "))

if age > 18:
    print(f"You can drive at age {age}")
