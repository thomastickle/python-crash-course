import json
from pathlib import Path

from util.exercise_output import print_exercise_header

BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = f"{BASE_DIR}/output/exercise_10_11.json"


def write_favorite_as_json(number: int):
    output_file = Path(FILE_NAME)
    output = json.dumps(number)
    try:
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
