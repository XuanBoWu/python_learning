import unittest
from employee_info import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("alex", "wu", 50000)
        self.original_annual_salary = self.my_employee.annual_salary
        return super().setUp()
    
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, self.original_annual_salary + 5000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, self.original_annual_salary + 10000)
        
if __name__ == '__main__':
    unittest.main()