from util.exercise_output import print_exercise_header


def describe_city(name: str, country: str = "England"):
    print(f"{name.title()} is in {country.title()}.")


print_exercise_header("8-5 Cities")

describe_city("Liverpool")
describe_city("New York", "United States of America")
describe_city("Manchester")
