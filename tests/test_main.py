from mental_math_teaser import main

import pytest


@pytest.mark.parametrize("trick_class", [clazz for clazz in main.ALL_TRICKS])
def test_all_tricks_instantiate(trick_class):
    # Check instantiating an instance of the class doesn't throw an error.
    trick = trick_class()

    # Verify it is actually an instance of the class.
    assert isinstance(trick, trick_class)
