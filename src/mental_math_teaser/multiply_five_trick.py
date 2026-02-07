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

    def trick_type_message(self):
        return (
            "Utilise the 'multiply by 5' trick. Here's how it works:\n"
            "* When squaring a number which ends in 5, strip the last '5' off both numbers, "
            "add 1 to one of the numbers, multiply both numbers together, then append 25. "
            "\n    Example: 65 * 65 = (6 * 7) + 25 = 4225\n"
            "* When multiplying two different numbers which end in 5, strip the last '5' off both numbers, "
            "multiply them together, then take the average of both numbers and add this to the previous "
            "multiplication, multiply this by 100 and add 25. "
            "\n    Example: 75 * 85 = (((7 * 8) + (7 + 8)/2) * 100) + 25 = ((56 + 7.5) * 100) + 25 = (63.5 * 100) + 25 "
            "= 6350 + 25 = 6375"
        )
