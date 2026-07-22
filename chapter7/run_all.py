from pathlib import Path
import re
import subprocess
import sys


def exercise_sort_key(path):
    exercise = path.stem.rsplit("_", 1)[1]
    match = re.fullmatch(r"(\d+)([a-z]*)", exercise)
    if match is None:
        raise ValueError(f"invalid exercise filename: {path.name}")
    return int(match.group(1)), match.group(2)


def main():
    chapter_directory = Path(__file__).parent
    project_directory = chapter_directory.parent
    for exercise in sorted(
        chapter_directory.glob("exercise_7_*.py"),
        key=exercise_sort_key,
    ):
        module = f"{chapter_directory.name}.{exercise.stem}"
        subprocess.run(
            [sys.executable, "-m", module],
            check=True,
            cwd=project_directory,
        )


if __name__ == "__main__":
    main()
