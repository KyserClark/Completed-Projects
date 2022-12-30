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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', ]


    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


sub_zero_ice_cream = IceCreamStand("Sub-Zero's Ice cream", 'ice cream')

sub_zero_ice_cream.describe_restaurant()
sub_zero_ice_cream.open_restaurant()
sub_zero_ice_cream.set_number_served(59)
print(sub_zero_ice_cream.number_served)
sub_zero_ice_cream.show_flavors()