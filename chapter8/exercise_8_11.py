from util.exercise_output import print_exercise_header


def show_messages(messages: list[str]):
    output = []
    while messages:
        message = messages.pop(0)
        print(f"Message was {message}.")
        output.append(message)
    return output


print_exercise_header("8-11 Sending Messages")

input_messages = ["hello", "goodbye", "you say"]
output_messages = show_messages(input_messages[:])

print("Input messages:")
for message in input_messages:
    print(f" - {message}")

print("\nOutput messages:")
for message in output_messages:
    print(f" - {message}")
