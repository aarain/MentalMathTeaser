import math

from mental_math_teaser.multiply_five_trick import MultiplyFiveTrick


def get_inputs_from_question_string(question):
    inputs = question.replace(" = ", "").split(" * ")
    return [int(s) for s in inputs]


def test_generate_question_and_answer():
    trick = MultiplyFiveTrick()
    assert math.prod(get_inputs_from_question_string(trick.question)) == int(
        trick.answer
    )


def test_answer_divisible_by_twenty_five():
    trick = MultiplyFiveTrick()
    assert int(trick.answer) % 25 == 0
