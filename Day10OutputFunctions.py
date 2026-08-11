#Functions with outputs

def my_function():
    result = 3 * 2
    return result
print(f"Result:  {my_function()}")


#Create a function that turns a first and last name into title case

f_name = input("What is your first name:  ")
l_name = input("What is your last name:  ")

def format_name(f_name, l_name):
    return((f_name + " " + l_name).title())

print(format_name(f_name, l_name))


#Returns true if a an inputted year is a leap year
def is_leap_year(year):
    '''This is a docstring, tells what a function is going to do
       this string can be mulilineThis is a docstring, tells what a function is going to do this string can be muliline''''
    if year % 400 == 0:
        return True

    if year % 100 == 0 and year % 4 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

'''
You can use this
as multiline comments as well.
'''

# You can store a reference to a function as a value to a veriable.
def add(n1, n2):
    return n1+n2

my_favorite_calculation = add
my_favorite_calculation(3,5)  #Will return 8

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
operation_symbol = input("Pick an operation: ")
answer = operations[operation_symbol](num1, num2)
# The name of the function is stored in the dictionary, which gets called by the
# chosen key, and then the n1 and n2 operations are passed to the value of the
# dictionary where "+" corresponds to a function called add(n1, n2)

