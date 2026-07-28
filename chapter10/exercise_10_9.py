from pathlib import Path

from util.exercise_output import print_exercise_header


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"


def getLinesFromFile(filename: str):
    input_file = INPUT_DIR / filename
    try:
        lines = input_file.read_text().rstrip().split("\n")
    except FileNotFoundError:
        return None
    else:
        return lines


print_exercise_header("10-9 Silent Cats and Dogs")
cat_file = getLinesFromFile("cats.txt")
if cat_file is None:
    quit()

dog_file = getLinesFromFile("dogs.txt")
if dog_file is None:
    quit()

output = cat_file + dog_file
for animal in output:
    print(f"Output file: {animal}.")
