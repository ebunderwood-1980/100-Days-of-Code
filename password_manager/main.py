from tkinter import *  # noqa F403, F405
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD -------------------------------
def add_password():
    # Get all of the data fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showwarning(title="Warning", message="Your website entry is missing")
    elif len(password) == 0:
        messagebox.showwarning(
            title="Warning", message="Your password entry is missing"
        )
    else:

        message_box_confirmation = messagebox.askokcancel(
            title=website,
            message=f"Data Entered: \nEmail: {email}\nPassword: {password}\nOkay to save?",
        )

        if message_box_confirmation:

            # Write the info to the file.
            with open("data.txt", "a") as password_storage:
                user_info = f"{website}  |  {email}  |  {password}\n"
                password_storage.write(user_info)

            # Clear the entry fields and focus back on the website
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Create the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=240, height=240)

# Bring in the Lock graphic
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Add in the Website user entry
website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(row=1, column=0)
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Add in the Email Username entry
email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
email_label.grid(row=2, column=0)
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "e.b.underwood@gmail.com")

# Add in the Password entry
password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(row=3, column=0)
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

# Add in the Generate Password Button
generate_button = Button(text="Generate Password", command=generate, width=15)
generate_button.grid(row=3, column=2)

# Creating the add button
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
