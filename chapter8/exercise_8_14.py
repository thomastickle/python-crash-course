from typing import Any
from util.exercise_output import print_exercise_header


def make_car(make: str, model: str, **options: Any) -> dict[str, Any]:
    car = {"make": make, "model": model, **options}
    return car


print_exercise_header("8-14 Cars")

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(f"Car: {car}")
