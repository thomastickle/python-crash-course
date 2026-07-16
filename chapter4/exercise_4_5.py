from exercise_output import print_exercise_header


print_exercise_header("4-5 Summing a Million")
one_to_million = list(range(1, 1000001))
print(f"one_to_million starts at {min(one_to_million)}")
print(f"one_to_million ends at {max(one_to_million)}")
print(f"one_to_million sums to {sum(one_to_million)}")
