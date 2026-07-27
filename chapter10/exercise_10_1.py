from pathlib import Path

from util.exercise_output import print_exercise_header


print_exercise_header("10-1 Learning Python")

path = Path("chapter10/learning_python.txt")
text = path.read_text().rstrip()
print(text)
