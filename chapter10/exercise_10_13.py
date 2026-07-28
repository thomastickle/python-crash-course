from util.exercise_output import print_exercise_header

from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
USER_FILE = OUTPUT_DIR / "exercise_10_13.json"


class User:
    def __init__(
        self,
        user_name: str,
        real_name: str | None,
        work_title: str | None,
    ) -> None:
        self.user_name = user_name
        self.real_name = real_name
        self.work_title = work_title


def get_stored_username(path: Path) -> User | None:
    try:
        contents = path.read_text(encoding="utf-8")
        stored_user: object = json.loads(contents)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    if not isinstance(stored_user, dict):
        return None

    user_name = stored_user.get("user_name")
    real_name = stored_user.get("real_name")
    work_title = stored_user.get("work_title")
    if (
        set(stored_user) != {"user_name", "real_name", "work_title"}
        or not isinstance(user_name, str)
        or (real_name is not None and not isinstance(real_name, str))
        or (work_title is not None and not isinstance(work_title, str))
    ):
        return None

    return User(user_name, real_name, work_title)


def save_user(path: Path, user: User) -> None:
    try:
        user_data = {
            "user_name": user.user_name,
            "real_name": user.real_name,
            "work_title": user.work_title,
        }
        json_rep = json.dumps(user_data, indent=4)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json_rep, encoding="utf-8")
    except FileNotFoundError:
        print(f"Unable to write to file {path}")
        quit()


def get_user_information() -> User:
    user_name = input("What is your name? ").strip()
    real_name = input("What is your real name? ").strip() or None
    work_title = input("What is your work title? ").strip() or None
    return User(user_name, real_name, work_title)


def greet_user() -> None:
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
        save_user(path, user)
        print(f"We'll remember you when you come back, {user.user_name}!")


print_exercise_header("10-13 User Dictionary.")

greet_user()
