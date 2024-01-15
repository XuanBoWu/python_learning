from attempt_login_count_9_5 import User

class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privilleges = Privileges()

    def show_privilleges(self):
        self.privilleges.show_privilleges()
    

class Privileges():
    def __init__(self):
        self.privilleges = ["can add post", "can delete post", "can ban user"]

    def show_privilleges(self):
        print("Administrator permissions are as follows:")
        for permission in self.privilleges:
            print(f"- {permission}")


admin = Admin("alex", "wu", "male", 25)

admin.show_privilleges()