from util.exercise_output import print_exercise_header


print_exercise_header("6-1 Person")

person = {
    "first_name": "Taylor",
    "last_name": "Swift",
    "age": 36,
    "city": "New York",
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
