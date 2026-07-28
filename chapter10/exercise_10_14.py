import json
from pathlib import Path

from util.exercise_output import print_exercise_header


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
USER_FILE = OUTPUT_DIR / "exercise_10_14.json"


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


def get_stored_username() -> User | None:
    try:
        contents = USER_FILE.read_text(encoding="utf-8")
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
    user_name = input("What is your user name? ").strip()
    real_name = input("What is your real name? ").strip() or None
    work_title = input("What is your work title? ").strip() or None
    return User(user_name, real_name, work_title)


def print_welcome_back(user: User) -> None:
    print(f"Welcome back, {user.user_name}!")
    print("I remember the following items about you: ")
    if user.real_name:
        print(f" - Real name: {user.real_name}")
    if user.work_title:
        print(f" - Work title: {user.work_title}")


def get_and_store_user_information() -> None:
    user = get_user_information()
    save_user(USER_FILE, user)
    print(f"We'll remember you when you come back, {user.user_name}!")


def greet_user() -> None:
    """Greet the user by name."""
    user = get_stored_username()
    if user:
        while True:
            decision = input(
                f"Is {user.user_name} the correct username?\nYes or No? "
            ).strip().casefold()
            if decision in {"y", "yes"}:
                print_welcome_back(user)
                return
            elif decision in {"n", "no"}:
                get_and_store_user_information()
                return
            else:
                print("Please answer 'yes' or 'no'.")
    else:
        get_and_store_user_information()


print_exercise_header("10-14 Verify User")
greet_user()
