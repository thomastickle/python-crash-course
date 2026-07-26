from chapter9.account_type import Admin

from util.exercise_output import print_exercise_header


print_exercise_header("9-11 Imported Admin")

user = Admin("Peter", "Parker", "/home/spiderman", "spiderman")

user.describe_user()
user.privileges.show_privileges()
