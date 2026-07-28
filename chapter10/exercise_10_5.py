from pathlib import Path

from util.exercise_output import print_exercise_header


print_exercise_header("10-5 Guest Book")
print("Please sign the guest book.")

guest_book: list[str] = []
while True:
    username = input("What is your name (Input 'quit' to finish): ")
    if username == "quit":
        break

    guest_book.append(username)

output = "\n".join(guest_book) + "\n"

output_directory = Path(__file__).resolve().parent
output_file = Path(f"{output_directory}/output/guest_book.txt")
output_file.write_text(output)
