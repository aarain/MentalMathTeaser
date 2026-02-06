from mental_math_teaser.main import get_welcome_message

import pytest


@pytest.mark.parametrize(
    "name, expected", [("Ashley", "Hi, Ashley!"), ("", "Hello, World!")]
)
def test_get_welcome_message(name, expected):
    assert get_welcome_message(name) == expected
