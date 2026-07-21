from util.exercise_output import print_exercise_header


print_exercise_header("6-6 Polling")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "c",
    "phil": "python",
}

people = ["mike", "jim", "jessica", "edward", "jen"]
normalized_names = {name.casefold() for name in favorite_languages}

for person in people:
    display_name = person.title()

    if person.casefold() in normalized_names:
        print(f"Thank you, {display_name}, for taking a poll")
    else:
        print(
            f"{display_name}, you are invited to take the poll "
            "on your favorite language."
        )
