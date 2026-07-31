import pytest

from chapter11.employee import Employee


@pytest.fixture
def employee() -> Employee:
    return Employee("Clark", "Kent", 100000)


def test_give_default_raise(employee: Employee) -> None:
    employee.give_raise()
    assert employee.annual_salary == 105000


def test_give_custom_raise(employee: Employee) -> None:
    employee.give_raise(20000)
    assert employee.annual_salary == 120000
