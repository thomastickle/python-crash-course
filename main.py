import argparse
import subprocess
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run Python Crash Course exercises."
    )
    parser.add_argument(
        "chapter",
        type=int,
        nargs="?",
        help="chapter number to run; omit to run every chapter",
    )
    parser.add_argument(
        "exercise",
        type=int,
        nargs="?",
        help="exercise number to run within the selected chapter",
    )
    return parser, parser.parse_args()


def run_script(script):
    subprocess.run([sys.executable, script], check=True)


def main():
    parser, args = parse_args()
    project_directory = Path(__file__).parent

    if args.chapter is not None:
        chapter_directory = project_directory / f"chapter{args.chapter}"
        chapter_runner = chapter_directory / "run_all.py"

        if not chapter_runner.is_file():
            parser.error(f"chapter {args.chapter} does not exist")

        if args.exercise is not None:
            exercise = chapter_directory / f"exercise_{args.chapter}_{args.exercise}.py"
            if not exercise.is_file():
                parser.error(
                    f"exercise {args.chapter}-{args.exercise} does not exist"
                )
            module = f"{chapter_directory.name}.{exercise.stem}"
            subprocess.run(
                [sys.executable, "-m", module],
                check=True,
                cwd=project_directory,
            )
            return

        run_script(chapter_runner)
        return

    for chapter_runner in sorted(
        project_directory.glob("chapter*/run_all.py"),
        key=lambda path: int(path.parent.name.removeprefix("chapter")),
    ):
        run_script(chapter_runner)


if __name__ == "__main__":
    main()
