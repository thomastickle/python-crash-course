from util.exercise_output import print_exercise_header


# Display a message about making a shirt with a size and message.
def make_shirt(size: str = "large", message: str = "I ❤️ Python!"):
    print(
        f"Making shirt of size {size.casefold()} with a message of '{message.title()}'."
    )


print_exercise_header("8-4 T-Shirt")

print("Calling the make_shirt function using default parameters.")
make_shirt()

print("Calling make_shirt with size medium but default parameters.")
make_shirt("medium")


print("Calling the make_shirt with size and different message.")
make_shirt(message="Java is 👑.", size="small")
