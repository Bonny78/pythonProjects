from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        # setting window color, padding
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # create canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        # canvas text
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Question here",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        # score label
        self.score_label = Label(text="Score: 0", fg="white", font=(FONT_NAME, 15, "normal"), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # add button
        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The Quiz is completed")
            self.true_pressed.config(state="disabled")
            self.false_pressed.config(state="disabled")



    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
