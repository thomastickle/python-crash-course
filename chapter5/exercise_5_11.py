from util.exercise_output import print_exercise_header


print_exercise_header("5-11 Ordinal Numbers")

numeric_list = list(range(1, 10))

for number in numeric_list:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
