break_line = "----------------------------------------------"

# 3-1
print(break_line)
print("3-1 Names")
friendNames = ["Joe", "Rosa", "Karen", "Matt"]
print(friendNames[0])
print(friendNames[1])
print(friendNames[3])

# 3-2
print(break_line)
print("3-2 Greetings")
message = "How are you, "
print(f"{message}{friendNames[0]}?")
print(f"{message}{friendNames[1]}?")
print(f"{message}{friendNames[2]}?")

# 3-3
print(break_line)
print("3-3 Your Own List")
transportation_methods = ["Bike", "Car", "Train"]
for transportation_method in transportation_methods:
    print(f"I would like to own a {transportation_method}")

# 3-4
print(break_line)
print("3-4 Guest List")
guest_list = ["Marcus Aurilias", "Thomas Aquinas", "Andrew Jackson"]
for guest in guest_list:
    print(f"Greetings {guest}, you are invited to a dinner with the Code Tickler.")

# 3-5
print(break_line)
print("3-5 Changing Guest List")
cannot_make = "Thomas Aquinas"
guest_list.remove(cannot_make)
new_guest = "Augustine of Hippo"
guest_list.append(new_guest)
for guest in guest_list:
    print(f"Greetings {guest}, you are invited to a dinner with the Code Tickler.")

# 3-6
print(break_line)
print("3-6 More Guests")
print("I was able to find a bigger table.  New invites to follow:")
guest_list.insert(0, "John Von Nuemman")
guest_list.insert(len(guest_list) // 2, "John Milton")
guest_list.append("Benjamin Franklin")
for guest in guest_list:
    print(f"Greetings {guest}, you are invited to a dinner with the Code Tickler.")

# 3-7
print(break_line)
print("3-7 Shrinking Guest List")
print("Sorry I can only invite two guests.")
while len(guest_list) > 2:
    guest = guest_list.pop()
    print(f"I'm sorry {guest}.  I am unable to invite you.")

for guest in guest_list:
    print(f"Congradulations {guest}.  You are still invited.")

del guest_list[0]
del guest_list[0]
print(guest_list)

# 3-8
print(break_line)
print("3-8 Seeing the World")
world_locations = [
    "Chichen Itza, Mexico",
    "Rome, Italy",
    "Corsica, France",
    "Singapore",
    "Yellowstone, Wyoming",
]
print(world_locations)
print(sorted(world_locations))
print(world_locations)
print(sorted(world_locations, reverse=True))
print(world_locations)
world_locations.reverse()
print(world_locations)
world_locations.reverse()
print(world_locations)
world_locations.sort()
print(world_locations)
world_locations.sort(reverse=True)
print(world_locations)

# 3-9
print(break_line)
print("3-9 Dinner Guests")
guest_list = ["Marcus Aurilias", "Thomas Aquinas", "Andrew Jackson"]
print(f"I am inviting {len(guest_list)} guests to dinner.")

# 3-10
print(break_line)
print("3-10 Every Function")
rivers = ["Mississippi", "Missouri", "Nile", "Amazon", "Euphrates"]
print(f"Rivers: {rivers}")
print(f"Sorted Rivers: {sorted(rivers)}")
print(f"Reverse Sorted Rivers: {sorted(rivers, reverse=True)}")
print(f"Rivers: {rivers}")
rivers.pop()
print(f"Rivers after pop: {rivers})")
rivers.append("Tigerus")
print(f"Rivers after adding Tigerus: {rivers}")
rivers.reverse()
print(f"Rivers after reverse(): {rivers}")
rivers.reverse()
print(f"Rivers after 2nd reverse(): {rivers}")
rivers.remove("Missouri")
print(f"Rivers after removing Missouri: {rivers}")
rivers.insert(3, "Yangtze")
print(f"Rivers after inserting Yangtze: {rivers}")
rivers.sort
print(f"Rivers after sorting: {rivers}")
