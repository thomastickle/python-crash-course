from util.exercise_output import print_exercise_header


print_exercise_header("6-9 Favorite Places")

favorite_places = {
    "mike": ["New Orleans", "Atlanta"],
    "jessica": ["Paris", "New York", "San Francisco"],
    "jim": ["Chicago"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"- {place}")
