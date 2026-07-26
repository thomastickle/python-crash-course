from chapter9.admin import Admin
from util.exercise_output import print_exercise_header

print_exercise_header("9-12 Multiple Modules")

user = Admin("Testy", "McTesterson", "/home/tmctesth", "tmctesth")
user.describe_user()
user.privileges.show_privileges()
