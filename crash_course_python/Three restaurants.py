class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is OPEN")

carls = Restaurant('carls', 'pizza')

billys = Restaurant('billys','burgers')

moopboop = Restaurant('moopboop', 'jello')

carls.describe_restaurant()

billys.describe_restaurant()

moopboop.describe_restaurant()

