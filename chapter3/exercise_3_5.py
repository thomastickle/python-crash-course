from util.exercise_output import print_exercise_header


print_exercise_header("3-5 Changing Guest List")
guest_list = ["Marcus Aurilias", "Thomas Aquinas", "Andrew Jackson"]
cannot_make = "Thomas Aquinas"
guest_list.remove(cannot_make)
new_guest = "Augustine of Hippo"
guest_list.append(new_guest)
for guest in guest_list:
    print(f"Greetings {guest}, you are invited to a dinner with the Code Tickler.")
