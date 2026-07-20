from util.exercise_output import print_exercise_header


print_exercise_header("6-2 Favorite number")

favorite_numbers = {
    "Alicia": 7,
    "Marcus": 13,
    "Priya": 4,
    "Daniel": 21,
    "Sofia": 9,
}

for name, favorite_number in favorite_numbers.items():
    print(f"{name} favorite number is {favorite_numbers}")
