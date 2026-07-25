from util.exercise_output import print_exercise_header


class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant} is open for business")


print_exercise_header("9-1 Restaurant")

restaurant = Restaurant("Umami", "Japanese")
restaurant.describe_restaurant()
restaurant.open_restaurant()
