import json
from pathlib import Path

from util.exercise_output import print_exercise_header


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
FAVORITE_NUMBER_FILE = OUTPUT_DIR / "exercise_10_11.json"


def read_favorite_number() -> int | None:
    file = FAVORITE_NUMBER_FILE
    try:
        input = file.read_text()
        value = json.loads(input)
        return value
    except FileNotFoundError:
        print(f"{file} not found")
        return None


print_exercise_header("10-11b Favorite Number")


favorite_number = read_favorite_number()
if favorite_number is not None:
    print(f"Your favorite number is: {favorite_number}")
