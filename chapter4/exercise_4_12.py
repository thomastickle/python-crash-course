from util.exercise_output import print_exercise_header

print_exercise_header("4-12 More Loops")
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(f"\t{food}")

print("My friends favorite foods are:")
for food in friends_foods:
    print(f"\t{food}")
