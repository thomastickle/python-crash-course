from random import sample

from util.exercise_output import print_exercise_header

numbers = list(range(1, 11))
letters = ["a", "b", "c", "d", "e"]
items: list[int | str] = numbers + letters

print_exercise_header("9-14 Lottery")

drawing = sample(items, 4)
print(f"Any ticket matching these 4 items {drawing} is a winner!")
