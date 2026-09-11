# ---------- Imports ------------
from tkinter import *
import random
import pandas


# --------- Constants and Globals ------------
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    words_list = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_list = pandas.read_csv("./data/french_words.csv")
finally:
    words_dictionary = words_list.to_dict(orient="records")


# ---------- Functions ----------
def check_pressed():
    """Removes known words from potential word list and saves new word list to words_to_learn.csv"""
    words_dictionary.remove(current_card)
    df = pandas.DataFrame(words_dictionary)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    """The function changes picks a random french word and displays it"""
    global words_dictionary, current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dictionary)
    card.itemconfig(language, text="French", fill="black")
    card.itemconfig(french_word, text=current_card["French"], fill="black")
    card.itemconfig(front_card, image=front_card_image)
    flip_timer = window.after(3000, update_card)


def update_card():
    """Flips over the current card to the 'back side' to display the English Translation"""
    global words_dictionary, current_card
    card.itemconfig(front_card, image=back_card_image)
    card.itemconfig(language, text="English", fill="white")
    card.itemconfig(french_word, fill="white", text=current_card["English"])


# ---------- UI Interface ----------
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Switching Loop
flip_timer = window.after(3000, update_card)

# Buttons
checkmark = PhotoImage(file="./images/right.png")
right_button = Button(
    image=checkmark,
    highlightthickness=0,
    borderwidth=0,
    relief="flat",
    command=check_pressed,
)
right_button.grid(row=1, column=1)
xmark = PhotoImage(file="./images/wrong.png")
wrong_button = Button(
    image=xmark,
    highlightthickness=0,
    borderwidth=0,
    relief="flat",
    command=next_card,
)
wrong_button.grid(row=1, column=0)

# Card Canvas
card = Canvas(
    height=526,
    width=800,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
)
front_card_image = PhotoImage(file="./images/card_front.png")
front_card = card.create_image(405, 265, image=front_card_image)
card.grid(row=0, column=0, columnspan=2)

# Front Card Labels
language = card.create_text(400, 150, font=("Arial", 40, "italic"), text="French")
french_word = card.create_text(
    400,
    263,
    font=("Arial", 60, "bold"),
)
next_card()

# Back Card Canvas
back_card_image = PhotoImage(file="./images/card_back.png")


# Keep Window Open
window.mainloop()
