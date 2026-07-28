from pathlib import Path

from util.exercise_output import print_exercise_header


def getLinesFromFile(filename: str):
    input_directory = Path(__file__).resolve().parent
    file = Path(f"{input_directory}/input/{filename}")
    try:
        lines = file.read_text().rstrip().split("\n")
    except FileNotFoundError:
        print(f"Unable to find {filename}")
        return None
    else:
        return lines


print_exercise_header("10-8 Cats and Dogs")
cat_file = getLinesFromFile("cats.txt")
if cat_file is None:
    quit()

dog_file = getLinesFromFile("dogs.txt")
if dog_file is None:
    quit()

output = cat_file + dog_file
for animal in output:
    print(f"Output file: {animal}.")
