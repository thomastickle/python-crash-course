from pathlib import Path

from util.exercise_output import print_exercise_header

print_exercise_header("10-2 Learning")

directory = Path(__file__).resolve().parent
file = Path(f"{directory}/learning_python.txt")
lines = file.read_text().rstrip().replace("Python", "C")
print(lines)
