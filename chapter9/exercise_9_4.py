from util.exercise_output import print_exercise_header


class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Numbers served: {self.number_served}")

    def open_restaurant(self):
        print(f"The {self.restaurant} is open for business")

    def set_number_served(self, number_served: int):
        self.number_served = number_served

    def increment_number_served(self):
        self.number_served += 1


print_exercise_header("9-4 Restaurant")

restaurant = Restaurant("Umami", "Japanese")
restaurant.describe_restaurant()
restaurant.number_served = restaurant.number_served + 1
restaurant.describe_restaurant()
restaurant.set_number_served(20)
restaurant.describe_restaurant()
restaurant.increment_number_served()
restaurant.describe_restaurant()
