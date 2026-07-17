from pathlib import Path
import subprocess
import sys


def main():
    chapter_directory = Path(__file__).parent
    project_directory = chapter_directory.parent
    for exercise in sorted(
        chapter_directory.glob("exercise_4_*.py"),
        key=lambda path: int(path.stem.rsplit("_", 1)[1]),
    ):
        module = f"{chapter_directory.name}.{exercise.stem}"
        subprocess.run(
            [sys.executable, "-m", module],
            check=True,
            cwd=project_directory,
        )


if __name__ == "__main__":
    main()
