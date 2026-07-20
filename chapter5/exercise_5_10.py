from util.exercise_output import print_exercise_header

print_exercise_header("5-10 Checking Usernames")

current_users = ["elmo", "bigbird", "oscar", "beaker", "kermit"]
new_users = ["misspiggy", "beaker", "gonzo", "grover", "kermit"]

current_users_lowercase = {s.casefold(): s for s in current_users}

for new_user in new_users:
    if new_user.casefold() in current_users_lowercase:
        print(f"I am sorry.  The {new_user} has already been used.")
    else:
        print(f"The {new_user} is available.")
