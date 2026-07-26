from chapter9.user import User


class Privileges:
    def __init__(self, privileges: list[str]):
        self.privilages = privileges

    def show_privileges(self):
        print(f"User permissions are as follows: {self.privilages}")


class Admin(User):
    def __init__(self, first_name, last_name, home_directory, userid):
        super().__init__(first_name, last_name, home_directory, userid)
        self.privileges = Privileges(
            [
                "can add post",
                "can delete post",
                "can ban user",
            ]
        )
