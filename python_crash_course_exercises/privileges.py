""" Contains the class Privileges only """


class Privileges:
    """ A model of what privileges could be """

    def __init__(self):
        self.privileges = ['can ban user', 'can add post', 'can delete post']

    def show_privileges(self):
        """ Lists all the privileges """

        for privilege in self.privileges:
            print("   >", privilege)
