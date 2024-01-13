class Dog:
    """ Try simulated puppy """

    def __init__(self, name, age):
        self.name = name.title()
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog("willie", 5)

my_dog.sit()
my_dog.roll_over()

