class Employee:
    def __init__(self, firstname: str, lastname: str, annual_salary: int):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, amount: int | None = None) -> None:
        if amount is None:
            self.annual_salary += 5000
        else:
            self.annual_salary += amount
