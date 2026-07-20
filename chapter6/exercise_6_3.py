from util.exercise_output import print_exercise_header


print_exercise_header("6-3 Glossary")

glossary = {
    "for": "Used to loop through a set number of items.",
    "if": "Used to do conditional branching based upon the predicate.",
    "range": "Method used to generate a range of values, can be set to increment by a certain amount.",
    "else": "When an if conditional fails, the else block runs.",
    "list": "Make a list out of a range of values.",
}

for key, value in glossary.items():
    print(f"{key}\n    - {value}")
