class Restaurant:

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant name is {self.restaurant_name}")
        print(f"cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")



my_restaurant = Restaurant("McDonald's", "Fried chicken and burgers")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()