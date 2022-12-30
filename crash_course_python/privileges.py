from user import User

class Privileges:
    def __init__(self):
        self.privileges = ['God Rights']

    def show_privileges(self):
        print(f"account has {self.privileges[0]}.")


class Admin(User):
    def __init__(self, first_name, last_name, location):
        super().__init__(first_name, last_name, location)
        self.privileges = Privileges()