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
        self.failed_logins = 0

    def describe_user(self):
        print("User:")
        print(f" - First name: ${self.first_name}")
        print(f" - Last name: {self.last_name}")
        print(f" - User ID: {self.attributes['user_id']}")
        print(f" - Home directory: {self.attributes['home_directory']}")
        print(f" - Number of failed logins: {self.failed_logins}")

    def greet_user(self):
        print(
            f"Greeting {self.first_name} {self.last_name}.  Hope you are doing well today."
        )

    def increment_login_attempts(self):
        self.failed_logins += 1

    def reset_login_attempts(self):
        self.failed_logins = 0


print_exercise_header("9-5 Login Attemmpts")

user = User("Louis", "Lane", "/home/llane", "llane")
user1 = User("Clark", "Kent", "/home/ckent", "ckent")
user2 = User("Bruce", "Wayne", "/home/batman", "batman")


print("Printing first user:")
user.describe_user()
user.increment_login_attempts()
user.describe_user()
user.increment_login_attempts()
user.describe_user()
user.increment_login_attempts()
user.describe_user()
user.increment_login_attempts()
user.reset_login_attempts()
user.describe_user()
