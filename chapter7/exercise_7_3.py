from util.exercise_output import print_exercise_header


print_exercise_header("7-3 Multiples of 10")
candidate = input("Please enter a number: ")
candidate = int(candidate)
if candidate % 10 == 0:
    print(f"{candidate} is a multiple of 10: ")
else:
    print(f"{candidate} is not a multiple of 10")
