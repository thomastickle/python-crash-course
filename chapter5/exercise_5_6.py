from util.exercise_output import print_exercise_header

print_exercise_header("5-6 Stages of Life")

person_age = 70

if person_age < 2:
    print("Person is a baby.")
elif 2 <= person_age and person_age < 4:
    print("Person is a toddler.")
elif 4 <= person_age and person_age < 13:
    print("Person is a child.")
elif 13 <= person_age and person_age < 20:
    print("Person is a teenage.")
elif 20 <= person_age and person_age < 65:
    print("Person is an adult.")
else: 
    print("Person is a senior.")

