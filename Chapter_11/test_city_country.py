import unittest
from city_function import formatted_city_country

class CityTestCase(unittest.TestCase):
    def test_city_name(self):
        formated_city_name = formatted_city_country("shenzhen", "china")
        self.assertEqual(formated_city_name, "Shenzhen, China")

    def test_city_population(self):
        formatted_name = formatted_city_country("shenzhen", "china", 20000000)
        self.assertEqual(formatted_name, "Shenzhen, China - population 20000000")
if __name__ == '__main__':
    unittest.main()