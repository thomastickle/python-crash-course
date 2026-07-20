from util.exercise_output import print_exercise_header

print_exercise_header("5-2 More Conditional Testing")

person = "John"
print("Is person == 'John'? I predict True.")
print(person == 'John')
print("Is person == 'Kate', I predict False.")
print(person == 'Kate')


print("Is person == 'John'? I predict True.")
print(person == 'John')
print("Is person == 'john'? I predice False.")
print(person.lower() == 'John')

print(f"Is 1 less than 2? {1 < 2}")
print(f"Is 2 less than 1? {2 < 1}")
print(f"Is 3 less than or equal to 5? {3 <= 4}")
print(f"Is 5 >= 1? { 5>=1}")

list = ["book", "pencil", "notebook"]
print(f"Is notebook in the list? {'notebook' in list}")
print(f"Is ruler in the list? {'ruler' in list}")
print(f"Is pen not in the list? {'pen' not in list}")
