from util.exercise_output import print_exercise_header


# Display a message about making a shirt with a size and message.
def make_shirt(size: str, message: str):
    print(
        f"Making shirt of size {size.casefold()} with a message of '{message.title()}'."
    )


print_exercise_header("8-3 T-Shirt")

print("Calling the make_shirt function using order specific parameters.")
make_shirt("large", "I ❤️ Python!")

print("Calling the make_shirt function using named parameters.")
make_shirt(message="I ❤️ Python!", size="large")
