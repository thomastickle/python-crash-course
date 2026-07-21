from util.exercise_output import print_exercise_header


print_exercise_header("6-8 Pets")

pet1 = {
    "name": "Buddy",
    "animal": "Dog",
    "owner": "Mike",
}

pet2 = {
    "name": "Whiskers",
    "animal": "Cat",
    "owner": "Jessica",
}

pet3 = {
    "name": "Goldie",
    "animal": "Goldfish",
    "owner": "Jim",
}

pet4 = {
    "name": "Charlie",
    "animal": "Parrot",
    "owner": "Sarah",
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()
