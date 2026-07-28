import json
from pathlib import Path

from util.exercise_output import print_exercise_header

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
FAVORITE_NUMBER_FILE = OUTPUT_DIR / "exercise_10_11.json"


def write_favorite_as_json(number: int):
    output_file = FAVORITE_NUMBER_FILE
    output = json.dumps(number)
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_file.write_text(output)
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


print_exercise_header("10-11a Favorite Number")


number = get_favorite_number()
if number is not None:
    write_favorite_as_json(number)
