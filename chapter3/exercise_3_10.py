from exercise_output import print_exercise_header


print_exercise_header("3-10 Every Function")
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
