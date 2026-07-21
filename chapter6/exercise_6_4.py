from util.exercise_output import print_exercise_header

print_exercise_header("6-4 Glossary 2")

print(
    "Turns out I already did this exercise as I did not want to create separate strings each time I wanted to print it."
)

glossary = {
    "for": "Used to loop through a set number of items.",
    "if": "Used to do conditional branching based upon the predicate.",
    "range": "Method used to generate a range of values, can be set to increment by a certain amount.",
    "else": "When an if conditional fails, the else block runs.",
    "list": "Make a list out of a range of values.",
}

for key, value in glossary.items():
    print(f"{key}\n    - {value}")
