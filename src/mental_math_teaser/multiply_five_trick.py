import random

from mental_math_teaser.trick_base import TrickBase


def generate_question_and_answer():
    a = random.randint(2, 20) * 5
    b = random.randint(2, 20) * 5
    r = a * b
    return f"{a} * {b} = ", str(r)


class MultiplyFiveTrick(TrickBase):
    def __init__(self):
        self.question, self.answer = generate_question_and_answer()
        super().__init__()
