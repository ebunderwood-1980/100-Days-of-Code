from tkinter import *  # noqa F403, F405


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    print("Generate Button Pressed")


# ---------------------------- SAVE PASSWORD -------------------------------
def add_password():
    # Get all of the data fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

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
