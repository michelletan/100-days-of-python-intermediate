from tkinter import Tk, Canvas, Label, PhotoImage
from tkmacosx import Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WINDOW_WIDTH = 350
WINDOW_HEIGHT = 500
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


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title = "Quiz Game"
        self.window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text="Score: ", font=SCORE_FONT_SETTINGS, bg=THEME_COLOR, pady=20)
        self.score_label.grid(row=0, column=1)

        self.question_canvas = Canvas(
            width=300, height=250, bg="white", border=0)

        self.question_text = self.question_canvas.create_text(
            150, 125, width=280, text="Question", fill=THEME_COLOR, font=QUESTION_FONT_SETTINGS, anchor="center")
        self.question_canvas.grid(row=1, column=0, columnspan=2, sticky='ew')

        img_button_right = PhotoImage(file=IMAGE_FILEPATH_ROOT + "true.png")
        img_button_wrong = PhotoImage(file=IMAGE_FILEPATH_ROOT + "false.png")

        self.btn_right = Button(image=img_button_right,
                                command=None, **BUTTON_OPTIONS)
        self.btn_wrong = Button(image=img_button_wrong,
                                command=None, **BUTTON_OPTIONS)

        self.btn_right.grid(row=2, column=0)
        self.btn_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        print(q_text)
        self.question_canvas.itemconfig(self.question_text, text=q_text)
