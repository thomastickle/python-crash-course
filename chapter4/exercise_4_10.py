from exercise_output import print_exercise_header

print_exercise_header("4-10 Slices")
animals = ["dog", "cat", "bird", "cow", "horse", "lizard", "snake"]
print(f"The first 3 items in the list are {animals[:3]}.")
print(f"The middle 3 items in the list are {animals[1:4]}")
print(f"The last 3 items int he list are {animals[-3:]}")
