from pathlib import Path

from util.exercise_output import print_exercise_header


print_exercise_header("10-4 Guest.")

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "guest.txt"

name = input("Please enter your name: ")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text(name)
