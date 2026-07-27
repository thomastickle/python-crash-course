from random import randint

from util.exercise_output import print_exercise_header


class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def roll_die(self):
        print(f"Value: {randint(1, self.sides)}")


print_exercise_header("9-13 Dice")

d6 = Die(6)
print("D6 Die Roll:")
for i in range(1, 10):
    d6.roll_die()

d10 = Die(10)
print("D10 Die Roll:")
for i in range(1, 10):
    d10.roll_die()

d20 = Die(20)
print("D20 Die Roll:")
for i in range(1, 10):
    d20.roll_die()
