import json
from pathlib import Path

from util.exercise_output import print_exercise_header

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
FAVORITE_NUMBER_FILE = OUTPUT_DIR / "exercise_10_12.json"


def write_favorite_as_json(number: int) -> None:
    output_file = FAVORITE_NUMBER_FILE
    output = json.dumps(number)
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_file.write_text(output, encoding="utf-8")
    except FileNotFoundError:
        print(f"Unable to write to file: {output_file}")
        return None


def get_favorite_number() -> int | None:
    number = input("What is your favorite number? ")
    try:
        return int(number)
    except ValueError:
        print(f"{number} was not an integer.")
        return None


def read_favorite_number() -> int | None:
    path = FAVORITE_NUMBER_FILE
    try:
        contents = path.read_text(encoding="utf-8")
        value: object = json.loads(contents)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    if isinstance(value, bool) or not isinstance(value, int):
        return None

    return value


print_exercise_header("10-12 Favorite Number Remembered")

favorite_number = read_favorite_number()
if favorite_number is None:
    favorite_number = get_favorite_number()
    if favorite_number is None:
        quit()
    else:
        write_favorite_as_json(favorite_number)

print(f"Your favorite number is: {favorite_number}")
