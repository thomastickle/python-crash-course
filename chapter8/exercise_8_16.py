from chapter8.car_functions import make_car
from util.exercise_output import print_exercise_header

print_exercise_header("8-16 Imports")


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(f"Car: {car}")
