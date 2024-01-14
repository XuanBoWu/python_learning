class User:
    def __init__(self, first_name, last_name, gender, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.first_name + " " + self.last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
         
        print(f"name: {self.name.title()}")
        print(f"gender: {self.gender}")
        print(f"age: {self.age}")

    def greet(self):
        print(f"Hello {self.name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User("alex", "wu", "male", 25)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)