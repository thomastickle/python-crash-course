from util.exercise_output import print_exercise_header


print_exercise_header("6-7 People")

person1 = {
    "first_name": "Taylor",
    "last_name": "Swift",
    "age": 36,
    "city": "New York",
}

person2 = {
    "first_name": "Keanu",
    "last_name": "Reeves",
    "age": 61,
    "city": "Los Angeles",
}

person3 = {
    "first_name": "Lionel",
    "last_name": "Messi",
    "age": 39,
    "city": "Miami",
}

persons = [person1, person2, person3]

for person in persons:
    print(f"{person['first_name']} {person['last_name']}")
    print(f"   Age : {person['age']}")
    print(f"   City : {person['city']}")
