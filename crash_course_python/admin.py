class User:
    def __init__(self, first_name, last_name, location):
        self.firstname = first_name
        self.lastname = last_name
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.firstname} {self.lastname} is from {self.location}.")

    def greet_user(self):
        print(f"Hello {self.firstname} {self.lastname}, how are you today?")

    def increment_login(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ['God Rights']

    def show_privileges(self):
        print(f"account has {self.privileges[0]}.")


class Admin(User):
    def __init__(self, first_name, last_name, location):
        super().__init__(first_name, last_name, location)
        self.privileges = Privileges()


kyser = Admin('admin', '', 'carrollton ohio')

kyser.privileges.show_privileges()
