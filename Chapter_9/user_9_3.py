class User:
    def __init__(self, first_name, last_name, gender, age, name='') -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.first_name + " " + self.last_name
        self.gender = gender
        self.age = age


    def describe_user(self):
         
        print(f"name: {self.name.title()}")
        print(f"gender: {self.gender}")
        print(f"age: {self.age}")

    def greet(self):
        print(f"Hello {self.name.title()}")

user_1 = User("alex", "wu", "male", 25)
user_2 = User("Jack", "love", "male", 23)
user_3 = User("justin","bieber", "male", 30)

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()