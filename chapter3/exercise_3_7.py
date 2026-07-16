from exercise_output import print_exercise_header


print_exercise_header("3-7 Shrinking Guest List")
guest_list = [
    "John Von Nuemman",
    "Marcus Aurilias",
    "John Milton",
    "Andrew Jackson",
    "Augustine of Hippo",
    "Benjamin Franklin",
]
print("Sorry I can only invite two guests.")
while len(guest_list) > 2:
    guest = guest_list.pop()
    print(f"I'm sorry {guest}.  I am unable to invite you.")

for guest in guest_list:
    print(f"Congradulations {guest}.  You are still invited.")

del guest_list[0]
del guest_list[0]
print(guest_list)
