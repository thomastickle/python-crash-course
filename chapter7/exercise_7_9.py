from util.exercise_output import print_exercise_header


print_exercise_header("7-9 No Pastrami")

sandwich_orders = [
    "BLT",
    "Pastrami",
    "Ham and Swiss",
    "Pastrami",
    "Italian",
    "Meatball",
    "Pastrami",
    "Club",
]
finished_sandwiches = []

print("The deli has run out of pastrami.")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich}")
