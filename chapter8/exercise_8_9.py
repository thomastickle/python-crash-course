from util.exercise_output import print_exercise_header


def show_messages(messages):
    for message in messages:
        print(f"Message was {message}.")


print_exercise_header("8-9 Messages")

messages = ["hello", "goodbye", "you say"]
show_messages(messages)
