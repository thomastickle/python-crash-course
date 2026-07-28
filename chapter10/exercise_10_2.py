from pathlib import Path

from util.exercise_output import print_exercise_header

print_exercise_header("10-2 Learning")

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input" / "learning_python.txt"

lines = INPUT_FILE.read_text(encoding="utf-8").rstrip().replace("Python", "C")
print(lines)
