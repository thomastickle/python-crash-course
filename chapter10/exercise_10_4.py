from pathlib import Path

from util.exercise_output import print_exercise_header


print_exercise_header("10-4 Guest.")


script_directory = Path(__file__).resolve().parent
output_file = Path(f"{script_directory}/output/guest.txt")

name = input("Please enter your name: ")
output_file.write_text(name)
