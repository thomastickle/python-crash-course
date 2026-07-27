from random import sample

from util.exercise_output import print_exercise_header

numbers = list(range(1, 11))
letters = ["a", "b", "c", "d", "e"]
items: list[int | str] = numbers + letters

print_exercise_header("9-15 Lottery Analysis")

ticket = set(sample(items, 4))

drawings = 0
while True:
    drawings += 1
    drawing = set(sample(items, 4))
    if drawing == ticket:
        break

print(f"It took {drawings} to win.")
