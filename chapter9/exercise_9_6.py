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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, flavors: list[str]):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = flavors

    def display_flavors(self):
        print(f"Flavors: {self.flavors}")


print_exercise_header("9-6 Ice Cream Stand")
ice_cream_stand = IceCreamStand("Frozen Creme", ["pistachio", "chocolate", "vanilla"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
