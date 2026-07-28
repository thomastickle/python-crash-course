from pathlib import Path

from util.exercise_output import print_exercise_header


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "guest_book.txt"


print_exercise_header("10-5 Guest Book")
print("Please sign the guest book.")

guest_book: list[str] = []
while True:
    username = input("What is your name (Input 'quit' to finish): ").strip()
    if username.casefold() == "quit":
        break

    guest_book.append(username)

output = "\n".join(guest_book)
if output:
    output += "\n"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text(output, encoding="utf-8")
