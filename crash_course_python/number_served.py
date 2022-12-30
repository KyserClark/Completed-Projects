class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is OPEN")

    def set_number_served(self, served):
        self.number_served += served


carls = Restaurant('carls', 'pizza')

carls.set_number_served(86)