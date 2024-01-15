from elerctric_car import Car

class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)
        self.battrey = Battery()

class Battery():
    def __init__(self, battery_capacity=75):
        self.battery_capacity = battery_capacity

    def set_battery_capacity(self, new_number):
        self.battery_capacity = new_number

    def describe_battery(self):
        print(f"This car has a {self.battery_capacity}-KWh battery.")

    def get_range(self):
        range = 0
        if self.battery_capacity == 75:
            range = 300
        elif self.battery_capacity == 100:
            range = 500

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_capacity != 100:
            self.battery_capacity = 100



    
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battrey.describe_battery()
my_tesla.battrey.get_range()

my_tesla.battrey.upgrade_battery()

my_tesla.battrey.describe_battery()
my_tesla.battrey.get_range()