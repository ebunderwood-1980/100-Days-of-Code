from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_LOCATION = "./images/true.png"
FALSE_LOCATION = "./images/false.png"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        # Create the Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            bg=THEME_COLOR,
            padx=20,
            pady=20,
        )

        # Create the Buttons
        true_image = PhotoImage(file=TRUE_LOCATION)
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            borderwidth=0,
            relief="flat",
            command=self.clicked_true,
        )
        self.true_button.grid(row=3, column=0)

        false_image = PhotoImage(file=FALSE_LOCATION)
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            borderwidth=0,
            relief="flat",
            command=self.clicked_false,
        )
        self.false_button.grid(row=3, column=1)

        # Create the Screen Canvas
        self.screen = Canvas(
            height=250,
            width=300,
            bg="white",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        self.screen.grid(row=1, column=0, columnspan=2, pady=20)

        # Add the question to the card
        self.question_text = self.screen.create_text(
            150,
            125,
            width=280,  # Allows the text to wrap after the width
            font=("Arial", 20, "italic"),
            text="text",
            fill=THEME_COLOR,
        )

        # Add the Score text
        self.score_label = Label(text=f"Score: {self.quiz.score}")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.get_next()

        self.window.mainloop()

    def get_next(self):
        self.screen.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.screen.itemconfig(self.question_text, text=q_text)
        else:
            self.screen.itemconfig(
                self.question_text, text="You have reached the end of the quiz"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def clicked_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.screen.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.screen.config(bg="red")

        self.window.after(1000, self.get_next)
