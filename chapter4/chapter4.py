#### Chapter 4: Looping ###

break_line = "----------------------------------------------"
# 4-1
print(break_line)
print("4-1 Pizza Types")
pizza_types = ["pepperoni", "italian sausage", "canadian bacon"]
for pizza in pizza_types:
    print(f"I like {pizza} pizza.")
print("I really love pizza")

# 4-2
print(break_line)
print("4-2 Animals")
animals = ["dog", "cat", "bird", "cow"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet.")

# 4-3
print(break_line)
print("4-3 Counting to 20")
for number in range(1, 21):
    print(number)

# 4-4
print(break_line)
print("4-4 One Million")
one_to_million = list(range(1, 1000001))
for number in one_to_million:
    print(number)

# 4-5
print(break_line)
print("4-5 Summing a Million")
print(f"one_to_million starts at {min(one_to_million)}")
print(f"one_to_million ends at {max(one_to_million)}")
print(f"one_to_million sums to {sum(one_to_million)}")


# 4-6
print(break_line)
print("4-6 Odd numbers.")
for number in range(1, 20, 2):
    print(number)

# 4-7
print(break_line)
print("4-7 Threes")
threes = list(range(3, 31, 3))
for three in threes:
    print(three)

# 4-8
print(break_line)
print("4-8 Cubes")
cubes = []
for value in range(1, 11):
    cubes.append(value**2)

for cube in cubes:
    print(cube)

# 4-9
print(break_line)
print("4-9 Cube Comprhesnion")
cubes = [value**2 for value in range(1, 11)]
print(cubes)


# 4-10
print(break_line)
print("4-10 Slices")
