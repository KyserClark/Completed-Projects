class User:
    def __init__(self, first_name, last_name, location):
        self.firstname = first_name
        self.lastname = last_name
        self.location = location

    def describe_user(self):
        print(f"{self.firstname} {self.lastname} is from {self.location}.")

    def greet_user(self):
        print(f"Hello {self.firstname} {self.lastname}, how are you today?")


kyser = User('kyser', 'clark', 'carrollton ohio')

kyser.describe_user()
kyser.greet_user()

kyser = User('chad', 'chillings', 'Australia')
elon = User('Elon', 'Musk', 'South Africa')
chef = User('Chef', 'Mark', 'kitchen')

elon.describe_user()
elon.greet_user()

chef.describe_user()
chef.greet_user()
