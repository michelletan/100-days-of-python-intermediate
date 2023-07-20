import html


class QuizBrain:
    """Contains question list and keeps track of score.
    Returns next question and score when prompted.

    Attributes:
        - question_number: Current question index
        - score: User's score in the game
        - question_list: List of questions
    """

    def __init__(self, question_list=[]) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def get_score(self) -> int:
        return self.score

    def get_current_question(self) -> str:
        return self.question_list[self.question_number - 1]

    def get_next_question(self) -> str:
        curr = self.question_list[self.question_number]
        self.question_number += 1
        return html.unescape(curr.question)

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.get_current_question().answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False

    def end_game(self) -> str:
        return f"Your final score is: {self.score}/{self.question_number}"
