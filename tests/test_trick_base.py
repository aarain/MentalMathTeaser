from freezegun import freeze_time

from mental_math_teaser.multiply_five_trick import MultiplyFiveTrick


@freeze_time("2026-02-07 12:00:00")
def test_get_elapsed_time_seconds():
    trick = MultiplyFiveTrick()

    with freeze_time("2026-02-07 12:01:00"):
        # The test now thinks one minute has passed instantly.
        assert trick.get_elapsed_time_seconds() == 60
