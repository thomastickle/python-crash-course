from pathlib import Path

from util.exercise_output import print_exercise_header


print_exercise_header("10-2 Learning")

file = Path("chapter10/learning_python.txt")
lines = file.read_text().rstrip().replace("Python", "C")
print(lines)
