""" This module contains the Restaurant and IcecreamStand classes.
    It is meant to practice the import of classes from a module.
"""

class Restaurant:
    """ Simple model of a restaurant """
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Provides a description of the restaurant. """
        info = f"{self.name.title()} is a restaurant specialized on"
        info += f" {self.cuisine_type.title()} cuisine."
        return info

    def open_restaurant(self):
        """ Tells if restaurant is open. """
        return f"{self.name.title()} is open."

    def set_number_served(self, number):
        """ Change the number of people served by the restaurant. """
        self.number_served = number

    def increment_number_served(self, number):
        """ Increment the number of people served with value given. """
        self.number_served += number


class IcecreamStand(Restaurant):
    """ Simple model of an ice cream stand, a kind of restaurant """
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla']

    def show_flavors(self):
        """ Shows the flavors available """
        print(' --- Flavors --- ')
        for flavor in self.flavors:
            print(flavor, end=', ')
        print()
        
    def add_flavors(self, flavors_list):
        """ Adds more flavors to the list """
        for flavor in flavors_list:
            self.flavors.append(flavor)
