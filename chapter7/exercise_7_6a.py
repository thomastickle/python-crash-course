from util.exercise_output import print_exercise_header


print_exercise_header("7-6 Three Exits Break Version")


print(
    "Please enter the age of the person for which you are buying the ticket."
    "Enter quit when done."
)
age = ""
while age != "quit":
    age = input("What is the age of the person: ")
    if age == "quit":
        continue
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif 3 <= age and age < 12:
            print("The ticket price is $10.")
        else:
            print("The ticket price is $15.")
