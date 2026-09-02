from tkinter import *


def button_click():
    new_text = my_input.get()
    top_label.config(text=new_text)


window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

top_label = Label(text="This is new text")
top_label.grid(row=0, column=0)


my_button = Button(text="Click Me", command=button_click)
my_button.grid(row=1, column=1)

my_input = Entry(width=20)
my_input.grid(row=2, column=3)

new_button = Button(text="This is the second button", command=button_click)
new_button.grid(row=0, column=2)

window.mainloop()


#  Pack vs. Place vs. Grid

# Place allow you to place in a specific spot, but is very tedios for large numbers of widgets.

# Grid
# Allows you to place widgets in by a column or row grid system.  You have to start with top left and work outwards.  You cannot use grid and pack in the same code.
