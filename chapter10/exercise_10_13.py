from util.exercise_output import print_exercise_header

from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
USER_FILE = OUTPUT_DIR / "exercise_10_13.json"


class User:
    def __init__(self, user_name: str, real_name: str | None, work_title: str | None):
        self.user_name = user_name
        self.real_name = real_name
        self.work_title = work_title


def get_stored_username(path) -> User | None:
    if path.exists():
        contents = path.read_text()
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
    user_name = input("What is your name? ")
    real_name = input("What is your real name? ")
    work_title = input("What is your work title? ")
    return User(user_name, real_name, work_title)


def greet_user():
    """Greet the user by name."""
    path = USER_FILE
    user = get_stored_username(path)
    if user:
        print(f"Welcome back, {user.user_name}!")
        print("I remember the following items about you: ")
        if user.real_name:
            print(f" - Real name: {user.real_name}")
        if user.work_title:
            print(f" - Work title: {user.work_title}")
    else:
        user = get_user_information()
        if user is not None:
            save_user(path, user)
            print(f"We'll remember you when you come back, {user.user_name}!")


print_exercise_header("10-13 User Dictionary.")

greet_user()
