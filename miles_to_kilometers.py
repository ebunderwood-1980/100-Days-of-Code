from tkinter import *

# Create a tkinter GUI that calculates the amount of kilometers from the user inputted number of miles.
# Will use text box, button, input box


# Calculate miles to kilometers function
def miles_to_kilos():
    miles = float(user_entry_box.get())
    kilometers = miles * 1.609
    kilo_answer.config(text=kilometers)


# Set up the background
calculator_background = Tk()
calculator_background.title("Miles to Kilometers Converter")
calculator_background.minsize(width=250, height=150)
calculator_background.config(padx=25, pady=25)

# Set up the is equal to label
is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)

# Set up the text entry box
user_entry_box = Entry(width=10)
user_entry_box.grid(row=0, column=1)
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# Set up the answer label
kilo_answer = Label(text="0")
kilo_answer.grid(row=1, column=1)
kilo_label = Label(text="Km")
kilo_label.grid(row=1, column=2)

# Set up the Calculate button
calculate_button = Button(text="Calculate", command=miles_to_kilos)
calculate_button.grid(row=2, column=1)


calculator_background.mainloop()
