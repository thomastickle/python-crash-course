from util.exercise_output import print_exercise_header


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add teh given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a batter for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Initialize attributes of the parent class."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


print_exercise_header("9-9 Battery Upgrade")
car = ElectricCar("Nissan", "Leaf", "2020")
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()
