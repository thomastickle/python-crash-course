from util.exercise_output import print_exercise_header


print_exercise_header("6-5 Rivers")

rivers = {
    "Mississippi": "United States of America",
    "Amazon": "Brazil",
    "Nile": "Egypt",
    "Ganges": "India",
    "Euphrates": "Iraq",
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}")

for river in rivers.keys():
    print(f"The river is {river}")
for country in rivers.values():
    print(f"The country is {country}")
