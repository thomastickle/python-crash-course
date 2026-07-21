from util.exercise_output import print_exercise_header


print_exercise_header("6-10 Favorite Numbers")

favorite_numbers = {
    "Alicia": [7],
    "Marcus": [13, 42],
    "Priya": [4, 29],
    "Daniel": [21, 69],
    "Sofia": [69, 420],
}

for person, favorite_numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")

    for number in favorite_numbers:
        print(f"  - {number}")
