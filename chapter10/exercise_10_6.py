from util.exercise_output import print_exercise_header


print_exercise_header("10-6 Addition")

print("Give me two numbers, I'll add them.")
first_input = input("\nFirst number: ").strip()
second_input = input("\nSecond number: ").strip()
try:
    first_number = int(first_input)
    second_number = int(second_input)
except ValueError:
    print("Both values must be integers. Please try again.")
else:
    result = first_number + second_number
    print(f"Sum is {result}.")
