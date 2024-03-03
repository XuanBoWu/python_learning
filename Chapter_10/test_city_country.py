import unittest
from city_function import formatted_city_country_name

class CityTestCase(unittest.TestCase):
    def test_city_name(self):
        formated_city_name = formatted_city_country_name("shenzhen", "china")
        self.assertEqual(formated_city_name, "Shenzhen, China")

if __name__ == '__main__':
    unittest.main()