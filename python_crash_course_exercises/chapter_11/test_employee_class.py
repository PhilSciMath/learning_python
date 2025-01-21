"""
Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.
"""

from employee_class import Employee
import pytest


# first approach, no fixture
def test_give_default_rise():
    """ Checks if a default rise of 5000 is correctly implemented. """
    employee = Employee('bruce', 'wayne', 1000000)
    employee.give_raise()
    assert employee.annual_salary == 1005000

def test_give_custom_raise():
    """ Checks if give_raise works for custom values. """
    employee = Employee('bruce', 'wayne', 1000000)
    employee.give_raise(999999)
    assert employee.annual_salary == 1999999


# second approach, using fixture decorator
# the advantage is that we don't need to create an instance in every test
@pytest.fixture
def employee_instance():
    """ This creates an instance of employee used by all tests bellow. """
    employee_instance = Employee('bruce', 'wayne', 1000000)
    return employee_instance

def test_give_default_rise_fixture(employee_instance):
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 1005000

def test_give_custom_raise_fixture(employee_instance):
    employee_instance.give_raise(999999)
    assert employee_instance.annual_salary == 1999999