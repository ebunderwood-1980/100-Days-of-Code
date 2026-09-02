# Tkinter
# -------

from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Create a label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()  # Places and centers label on the screen.

my_label["text"] = "New text"
my_lable.config(text="New text")


# Button
def button_clicked():
    new_text = input.get()  # Gets the text from the input box 'input'
    my_lable.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.pack()

window.mainloop()  # Keeps the window on the screen.  Must be at the very end of the program.

# Entry -- Input
input = Entry(width=10)
input.pack()


# Kwargs - Keyword Arguments
# ------


def my_function(a=1, b=2, c=3):
    pass


# You can now call my_function(), my_function(a=1), my_function(a=1, c=3), etc. because my_function is set with default values.


# Unlimited arguments
def add_example(
    *args,
):  # With the *args, you can enter as many arguements to the function as you would like.
    for n in args:
        print(n)


# Create an add function that will take as many arguements as you would like and will return the sum of those arguments.
def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


print(add(1, 2, 3, 6, 9))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    n += kwargs["add"]  # 2 + 3 = 5
    n *= kwargs["multiply"]  # 2 * 6 = 12


calculate(2, add=3, multiply=6)  # Creates a dictionary {"add": 3, "multiply":6}


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get(
            "model"
        )  # .get works just like kw["model"] but will return None if an argument was not provided, instead of crashing


my_car = Car(make="Nissan", model="GTT")
