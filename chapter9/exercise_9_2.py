from util.exercise_output import print_exercise_header


class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open for buisiness")


print_exercise_header("9-2 Three Restaurants")

restaurant = Restaurant("Umami", "Japanese")
restaurant2 = Restaurant("Calmari Pies", "Pizza")
restaurant3 = Restaurant("The French Connection", "French")
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
