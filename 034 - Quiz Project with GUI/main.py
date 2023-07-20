import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

QUIZ_URL = "https://opentdb.com/api.php"
QUIZ_SETTINGS = {
    "amount": 15,
    "category": 17,
    "type": "boolean"
}

question_bank = []


def populate_questions():
    global question_bank
    response = requests.get(url=QUIZ_URL, params=QUIZ_SETTINGS)
    data = response.json()
    for q in data["results"]:
        question_bank.append(Question(q["question"], q["correct_answer"]))


def main():
    populate_questions()

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    # while quiz.still_has_questions():
    #     quiz.next_question()

    quiz.end_game()


main()
