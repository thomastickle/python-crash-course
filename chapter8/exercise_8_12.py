from util.exercise_output import print_exercise_header


def make_sandwich(*items_wanted) -> None:
    print("You wanted the following items on your sandwich.")
    for item in items_wanted:
        print(f" - {item}")


print_exercise_header("8-12 Sandwiches")

make_sandwich("mustard", "mayo", "turkey")

make_sandwich("swiss cheese", "mustard", "ham")

make_sandwich("provolone", "oregano", "pepperoni", "olive oil", "salami")
