from util.exercise_output import print_exercise_header


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        home_directory: str,
        user_id: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = {"home_directory": home_directory, "user_id": user_id}

    def describe_user(self):
        print("User:")
        print(f" - First name: ${self.first_name}")
        print(f" - Last name: {self.last_name}")
        print(f" - User ID: {self.attributes['home_directory']}")
        print(f" - Home directory: {self.attributes['user_id']}")

    def greet_user(self):
        print(
            f"Greeting {self.first_name} {self.last_name}.  Hope you are doing well today."
        )


print_exercise_header("9-3 Users")

user = User("Louis", "Lane", "/home/llane", "llane")
user1 = User("Clark", "Kent", "/home/ckent", "ckent")
user2 = User("Bruce", "Wayne", "/home/batman", "batman")


print("Printing first user:")
user.describe_user()
user.greet_user()
print("Printing second user:")
user1.describe_user()
user1.greet_user()
print("Printing third user:")
user2.describe_user()
user2.greet_user()
