from util.exercise_output import print_exercise_header

print_exercise_header("5-8 Hello Admin")

user_list = ["thomas", "jessica", "mark", "admin", "mena"]

for user in user_list: 
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')
