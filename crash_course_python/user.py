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