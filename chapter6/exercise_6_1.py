from util.exercise_output import print_exercise_header


print_exercise_header("6-1 Person")

person = {
    "first_name": "Joe",
    "last_name": "Huang",
    "age": 46,
    "city": "Lawrenceville",
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
