from count_diners_9_4 import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["mango", "pineapple", "watermelon"]

    def print_flavors_info(self):
        print("Available flavors are as follows:")
        for flavor in self.flavors:
            print(f"- {flavor}")
        

my_icecream_stand = IceCreamStand("Mixue", "Ice Cream")

my_icecream_stand.print_flavors_info()

