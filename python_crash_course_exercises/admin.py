""" This class contains only the Admin class """


from user import User
from privileges import Privileges


class Admin(User):
    """ A model of what an admin user is """
    def __init__(self, first_name, last_name, age, function):
        super().__init__(first_name, last_name, age, function)
        self.privileges = Privileges()

