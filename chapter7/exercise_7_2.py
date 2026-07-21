from util.exercise_output import print_exercise_header


print_exercise_header("7-2 Restarurant Seating")

party_size = input("How many people are in your dinner party? ")
party_size = int(party_size)
if party_size > 8:
    print("Just one moment, we will have to get a table ready for you.")
else:
    print("Your table is ready")
