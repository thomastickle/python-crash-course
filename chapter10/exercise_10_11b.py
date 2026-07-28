import json
from pathlib import Path

from util.exercise_output import print_exercise_header


BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = f"{BASE_DIR}/output/exercise_10_11.json"


def read_favorite_number() -> int | None:
    file = Path(FILE_NAME)
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
