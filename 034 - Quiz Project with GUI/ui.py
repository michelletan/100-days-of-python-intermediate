from tkinter import Tk, Canvas, Label, PhotoImage
from tkmacosx import Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WINDOW_WIDTH = 350
WINDOW_HEIGHT = 500
CANVAS_BACKGROUND_COLOR = "white"
SCORE_FONT_SETTINGS = ("Arial", 15)
QUESTION_FONT_SETTINGS = ("Arial", 20, "italic")
BUTTON_OPTIONS = {
    "bg": THEME_COLOR,
    "activebackground": THEME_COLOR,
    "focusthickness": 0,
    "borderless": True,
    "pady": 20
}
IMAGE_FILEPATH_ROOT = "./images/"
QUESTION_INTERVAL = 1000  # ms


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title = "Quiz Game"
        self.window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text="Score: 0", font=SCORE_FONT_SETTINGS, bg=THEME_COLOR, pady=20)
        self.score_label.grid(row=0, column=1)

        self.question_canvas = Canvas(
            width=300, height=250, bg=CANVAS_BACKGROUND_COLOR, border=0)

        self.question_text = self.question_canvas.create_text(
            150, 125, width=280, text="Question", fill=THEME_COLOR, font=QUESTION_FONT_SETTINGS, anchor="center")
        self.question_canvas.grid(row=1, column=0, columnspan=2, sticky='ew')

        img_button_right = PhotoImage(file=IMAGE_FILEPATH_ROOT + "true.png")
        img_button_wrong = PhotoImage(file=IMAGE_FILEPATH_ROOT + "false.png")

        self.btn_right = Button(image=img_button_right,
                                command=self.on_right_btn_clicked, **BUTTON_OPTIONS)
        self.btn_wrong = Button(image=img_button_wrong,
                                command=self.on_wrong_btn_clicked, **BUTTON_OPTIONS)

        self.btn_right.grid(row=2, column=0)
        self.btn_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg=CANVAS_BACKGROUND_COLOR)
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.get_next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.show_end_game()

    def on_right_btn_clicked(self):
        if self.quiz_brain.still_has_questions():
            ans_status = self.quiz_brain.check_answer(True)
            self.give_feedback(ans_status)

    def on_wrong_btn_clicked(self):
        if self.quiz_brain.still_has_questions():
            ans_status = self.quiz_brain.check_answer(False)
            self.give_feedback(ans_status)

    def update_score(self):
        score = self.quiz_brain.get_score()
        self.score_label.config(text=f"Score: {score}")

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.update_score()
        self.window.after(QUESTION_INTERVAL, self.get_next_question)

    def show_end_game(self):
        self.btn_right.configure(command=None)
        self.btn_wrong.configure(command=None)
        self.question_canvas.config(bg=CANVAS_BACKGROUND_COLOR)

        final_text = self.quiz_brain.end_game()
        self.question_canvas.itemconfig(self.question_text, text=final_text)
