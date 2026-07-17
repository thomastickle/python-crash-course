from util.exercise_output import print_exercise_header


print_exercise_header("3-6 More Guests")
guest_list = ["Marcus Aurilias", "Andrew Jackson", "Augustine of Hippo"]
print("I was able to find a bigger table.  New invites to follow:")
guest_list.insert(0, "John Von Nuemman")
guest_list.insert(len(guest_list) // 2, "John Milton")
guest_list.append("Benjamin Franklin")
for guest in guest_list:
    print(f"Greetings {guest}, you are invited to a dinner with the Code Tickler.")
