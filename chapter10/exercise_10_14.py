import json
from pathlib import Path

from util.exercise_output import print_exercise_header


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
USER_FILE = OUTPUT_DIR / "exercise_10_14.json"


class User:
    def __init__(self, user_name: str, real_name: str | None, work_title: str | None):
        self.user_name = user_name
        self.real_name = real_name
        self.work_title = work_title


def get_stored_username() -> User | None:
    if USER_FILE.exists():
        contents = USER_FILE.read_text()
        username = json.loads(contents)
        return User(**username)
    else:
        return None


def save_user(path: Path, user: User):
    try:
        json_rep = json.dumps(user.__dict__, indent=4)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json_rep)
    except FileNotFoundError:
        print(f"Unable to write to file {path}")
        quit()


def get_user_information() -> User:
    user_name = input("What is your user name? ")
    real_name = input("What is your real name? ")
    work_title = input("What is your work title? ")
    return User(user_name, real_name, work_title)


def print_welcome_back(user: User):
    print(f"Welcome back, {user.user_name}!")
    print("I remember the following items about you: ")
    if user.real_name:
        print(f" - Real name: {user.real_name}")
    if user.work_title:
        print(f" - Work title: {user.work_title}")


def get_and_store_user_information():
    user = get_user_information()
    if user is not None:
        save_user(USER_FILE, user)
        print(f"We'll remember you when you come back, {user.user_name}!")


def greet_user():
    """Greet the user by name."""
    user = get_stored_username()
    if user:
        decision = input(f"Is {user.user_name} the correct username?\nYes or No? ")
        if decision.casefold() == "Yes".casefold():
            print_welcome_back(user)
        else:
            get_and_store_user_information()
    else:
        get_and_store_user_information()


print_exercise_header("10-14 Verify User")
greet_user()
