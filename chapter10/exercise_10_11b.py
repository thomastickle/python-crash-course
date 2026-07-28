import json
from pathlib import Path

from util.exercise_output import print_exercise_header


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
FAVORITE_NUMBER_FILE = OUTPUT_DIR / "exercise_10_11.json"


def read_favorite_number() -> int | None:
    path = FAVORITE_NUMBER_FILE
    try:
        contents = path.read_text(encoding="utf-8")
        value: object = json.loads(contents)
    except FileNotFoundError:
        print(f"{path} not found")
        return None
    except json.JSONDecodeError:
        print(f"{path} does not contain valid JSON")
        return None

    if isinstance(value, bool) or not isinstance(value, int):
        print(f"{path} does not contain an integer")
        return None

    return value


print_exercise_header("10-11b Favorite Number")


favorite_number = read_favorite_number()
if favorite_number is not None:
    print(f"Your favorite number is: {favorite_number}")
