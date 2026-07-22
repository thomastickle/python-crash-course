from collections import Counter

from util.exercise_output import print_exercise_header


print_exercise_header("7-10 Dream Vacation")

polled_people = ["Mary", "Kate", "Mason", "John", "Rosa"]

destinations = Counter(
    input(
        f"{person}, if you could visit one place in the world, where would you go? "
    ).strip()
    for person in polled_people
)

print("\nVacation destinations by number of votes:")

for location, count in destinations.items():
    print(f" - {location}: {count}")
