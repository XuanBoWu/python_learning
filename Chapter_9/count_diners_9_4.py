class Restaurant:

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"restaurant name is {self.restaurant_name}")
        print(f"cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"Number served is {self.number_served}")

    def increment_number_served(self, increment_number):
        self.number_served += increment_number



if __name__ == '__main__':
    my_restaurant = Restaurant("McDonald's", "Fried chicken and burgers")

    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

    my_restaurant.set_number_served(10)

    my_restaurant.increment_number_served(20)

    print(my_restaurant.number_served)