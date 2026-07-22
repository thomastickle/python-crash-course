from util.exercise_output import print_exercise_header


print_exercise_header("7-4 Pizza Toppings")

print(
    "Please enter a topping followed by enter. When you are finished, please type quit."
)

prompt_message = "Please enter a topping: "
topping = ""
while topping != "quit":
    topping = input(prompt_message)
    if topping == "quit":
        break
    print(f"{topping} will be added to the pizza.")
