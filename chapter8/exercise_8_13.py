from typing import Any

from util.exercise_output import print_exercise_header


def build_profile(first: str, last: str, **user_info: Any) -> dict[str, Any]:
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


print_exercise_header("8-13 User Profile")

user_info = build_profile(
    "Thomas", "Tickle", city="Dallas", state="Georgia", employment_status="unemployed"
)

print(user_info)
