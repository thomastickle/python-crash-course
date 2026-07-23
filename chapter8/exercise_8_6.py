from util.exercise_output import print_exercise_header


def city_country(city: str, country: str):
    return f"{city.title()}, {country.title()}"


print_exercise_header("8-6 City Names")

print(f"{city_country('New York', 'United States of America')}")
print(f"{city_country('London', 'England')}")
print(f"{city_country('Paris', 'France')}")
