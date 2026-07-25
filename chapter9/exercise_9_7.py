from util.exercise_output import print_exercise_header


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        home_directory: str,
        userid: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.home_directory = home_directory
        self.userid = userid
        self.failed_logins = 0

    def describe_user(self):
        print("User:")
        print(f" - First name: {self.first_name}")
        print(f" - Last name: {self.last_name}")
        print(f" - User ID: {self.userid}")
        print(f" - Home directory: {self.home_directory}")
        print(f" - Number of failed logins: {self.failed_logins}")

    def greet_user(self):
        print(
            f"Greeting {self.first_name} {self.last_name}.  Hope you are doing well today."
        )

    def increment_login_attempts(self):
        self.failed_logins += 1

    def reset_login_attempts(self):
        self.failed_logins = 0


class Admin(User):
    def __init__(self, first_name, last_name, home_directory, userid):
        super().__init__(first_name, last_name, home_directory, userid)
        self.permissions = [
            "can add post",
            "can delete post",
            "can ban user",
        ]

    def show_permissions(self):
        print(f"User permissions are as follows: {self.permissions}")


print_exercise_header("9-7 Admin")

user = Admin("Louis", "Lane", "/home/llane", "llane")

print("Printing first user:")
user.describe_user()
user.show_permissions
