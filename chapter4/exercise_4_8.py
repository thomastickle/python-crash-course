from util.exercise_output import print_exercise_header


print_exercise_header("4-8 Cubes")
cubes = []
for value in range(1, 11):
    cubes.append(value**2)

for cube in cubes:
    print(cube)
