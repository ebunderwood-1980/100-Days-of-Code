from tkinter import *
import math

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
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    timer_label.place(x=100, y=-40)
    canvas.itemconfig(timer_text, text="0:00")
    complete_pomodoros.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    REPS += 1

    if REPS % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work")
    elif REPS == 8:
        count_down(long_break)
        timer_label.config(text="Long Break", fg=RED)
        timer_label.place(x=60, y=-40)
    elif REPS % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Short Break", fg=PINK)
        timer_label.place(x=52, y=-40)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    global timer

    minutes = math.floor(count / 60)
    seconds = count % 60
    adjusted_timer = f"{minutes}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=adjusted_timer)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(REPS / 2)):
            marks += CHECK_MARK
        complete_pomodoros.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=0, pady=50, bg=YELLOW)
window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()

timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold")
)


timer_label = Label(text="Timer")
timer_label.config(font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.place(x=100, y=-40)


start_button = Button()
start_button.config(
    text="Start",
    font=(FONT_NAME, 8, "bold"),
    bg="white",
    fg="blue",
    highlightthickness=0,
    command=start_timer,
)
start_button.place(x=30, y=215)


stop_button = Button()
stop_button.config(
    text="Reset",
    font=(FONT_NAME, 8, "bold"),
    bg="white",
    fg="blue",
    command=reset_timer,
    highlightthickness=0,
)
stop_button.place(x=225, y=213)

complete_pomodoros = Label()
complete_pomodoros.config(width=10, fg=GREEN, bg=YELLOW)
complete_pomodoros.place(x=112, y=230)

window.mainloop()
