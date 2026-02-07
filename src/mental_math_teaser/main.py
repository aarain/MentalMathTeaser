import random

from mental_math_teaser.multiply_five_trick import MultiplyFiveTrick

EXIT_CODES = ["quit", "q"]
HINT_CODES = ["trick", "t"]


def codes_to_string(codes):
    quoted_codes = [f"'{code}'" for code in codes]
    return " or ".join(quoted_codes)


def intro_message():
    return (
        "****** Welcome to the Mental Math Teaser! ******\n"
        f"If this all gets a bit much for you, answer with {codes_to_string(EXIT_CODES)} to end this session.\n"
        "If you would like a hint explaining which trick to use and how to use it,"
        f" answer with {codes_to_string(HINT_CODES)}.\n"
        "Otherwise, I hope your brain is switched on because there's no time for warm-ups...\n"
    )


# Add new tricks to this list as necessary.
ALL_TRICKS = [MultiplyFiveTrick]


def generate_trick():
    SelectedClass = random.choice(ALL_TRICKS)
    return SelectedClass()


def main():
    print(intro_message())

    trick = generate_trick()

    while True:
        command = input(trick.question)

        if command in EXIT_CODES:
            print("\n****** Thanks for stopping by! ******")
            exit(0)
        elif command in HINT_CODES:
            print(f"\n{trick.trick_type_message()}\n")
        elif command == trick.answer:
            print("\nCorrect! Here's another...")
            trick = generate_trick()
        else:
            print("Wrong! Try again...")


if __name__ == "__main__":
    main()
