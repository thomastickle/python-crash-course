from typing import Any


def make_car(make: str, model: str, **options: Any) -> dict[str, Any]:
    car = {"make": make, "model": model, **options}
    return car
