class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.name = f"{first_name} {last_name}"
        self.annual_salary = annual_salary
    
    def give_raise(self, annual_salary_increase=5000):
        self.annual_salary += annual_salary_increase
    

    

        