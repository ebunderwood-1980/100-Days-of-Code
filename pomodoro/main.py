from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=0, pady=50, bg=YELLOW)
window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()

canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))

timer_label = Label(text="Timer")
timer_label.config(font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.place(x=100, y=-40)


start_button = Button()
start_button.config(
    text="Start",
    font=(FONT_NAME, 8, "bold"),
    bg="white",
    fg="blue",
)
start_button.place(x=30, y=215)


stop_button = Button()
stop_button.config(
    text="Stop",
    font=(FONT_NAME, 8, "bold"),
    bg=YELLOW,
    fg="blue",
)
stop_button.place(x=225, y=213)

complete_pomodoros = Label()
complete_pomodoros.config(width=10, fg=GREEN, bg=YELLOW)
complete_pomodoros.place(x=112, y=230)

window.mainloop()
