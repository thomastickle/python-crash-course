from util.exercise_output import print_exercise_header


print_exercise_header("6-11 Cities")

cities = {
    "new orleans": {
        "country": "United States",
        "population": 364000,
        "fact": "Known for Mardi Gras and its unique Creole and Cajun culture.",
    },
    "paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Home to the Eiffel Tower and the Louvre Museum.",
    },
    "tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "The world's largest metropolitan area.",
    },
}

for city, facts in cities.items():
    print(f"{city}:")

    for title, information in facts.items():
        print(f" - {title.title()}: {information}")
