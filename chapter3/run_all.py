from pathlib import Path
import subprocess
import sys


def main():
    chapter_directory = Path(__file__).parent
    for exercise in sorted(
        chapter_directory.glob("exercise_3_*.py"),
        key=lambda path: int(path.stem.rsplit("_", 1)[1]),
    ):
        subprocess.run([sys.executable, exercise], check=True)


if __name__ == "__main__":
    main()
