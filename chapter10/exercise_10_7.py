from util.exercise_output import print_exercise_header


def get_integer(prompt: str) -> int | None:
    while True:
        value = input(prompt).strip()
        if value.casefold() == "quit":
            return None

        try:
            return int(value)
        except ValueError:
            print(f"{value!r} is not a valid integer.  Try again.")


def main() -> None:
    print_exercise_header("10-7 Addition Calculator")

    print("Give me two numbers, I'll add them.")
    print("Enter 'quit' at either prompt to stop")
    while True:
        first_number = get_integer("\nFirst number: ")

        if first_number is None:
            break

        second_number = get_integer("\nSecond number: ")

        if second_number is None:
            break

        result = first_number + second_number
        print(f"Sum is {result}.")

    print("Goodbye!")


if __name__ == "__main__":
    main()
