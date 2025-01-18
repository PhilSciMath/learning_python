""" Contains the classes Privileges, User and Admin """


class Privileges:
    """ A class containing privileges """

    def __init__(self):
        self.privileges = ['can ban user', 'can add post', 'can delete post']

    def show_privileges(self):
        """ Shows the list of privileges """
        for privilege in self.privileges:
            print("   >", privilege)


class User:
    """ A simple model of a user """

    def __init__(self, first_name, last_name, age, function):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.function = function
        self.login_attempts = 0

    def describe_user(self):
        """ Provides a description of the user """
        info = f"{self.first_name.title()} {self.last_name.title()} is "
        info += f"{self.age} years old, and is a {self.occupation}."
        return info

    def increment_login_attempts(self):
        """ Increments login attempts adding 1 each time """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Set login attempts back to 0 """
        self.login_attempts = 0

    def gret_user(self):
        """ Prints a message to the user """
        print(f"Hello, {self.first_name.title()}!")


class Admin(User):
    """ Model of a special user, the admin """

    def __init__(self, first_name, last_name, age, function):
        super().__init__(first_name, last_name, age, function)
        self.privileges = Privileges()
