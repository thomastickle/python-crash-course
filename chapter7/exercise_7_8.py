from util.exercise_output import print_exercise_header


print_exercise_header("7-8 Deli")

sandwich_orders = ["BLT", "Ham and Swiss", "Italian", "Meatball", "Club"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich}")
