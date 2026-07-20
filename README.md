# Python Crash Course Exercises

This repository contains my solutions to the exercises from *Python Crash Course*,
starting with chapter 2. Each exercise is a standalone Python script, and each
chapter includes a runner for executing all of its exercises in order.

## Requirements

- Python 3
- No third-party packages are required

Run the commands below from the repository's top-level directory.

## Run every exercise

```bash
python3 main.py
```

This runs each chapter in numerical order.

> **Note:** Chapter 4 exercise 4-4 prints every number from 1 through 1,000,000,
> so running all exercises produces a large amount of terminal output.

## Run one chapter

Pass a chapter number to the top-level runner:

```bash
python3 main.py 2
python3 main.py 3
python3 main.py 4
python3 main.py 5
```

## Run one exercise

Pass both the chapter and exercise numbers to the top-level runner. For example:

```bash
python3 main.py 2 1
python3 main.py 3 7
python3 main.py 4 10
python3 main.py 5 1
```

Exercises can also be run as Python modules from the repository root:

```bash
python3 -m chapter5.exercise_5_1
```

Use `python3 main.py --help` to see the available arguments.

Each exercise prints a heading before its output so exercises are easy to
distinguish when a chapter or the entire repository is run at once.
