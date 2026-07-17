from util.exercise_output import print_exercise_header

print_exercise_header("4-11 My Pizzas, Your Pizzas")
my_pizzas = ["pepperoni", "italian sausage", "canadian bacon"]
friends_pizzas = my_pizzas[:]

my_pizzas.append("meat lovers")
friends_pizzas.append("hawaiian")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"\t{pizza}")

print("My friends favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"\t{pizza}")
