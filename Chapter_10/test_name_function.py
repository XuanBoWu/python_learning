import unittest

from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test 'name_function.py'"""

    def test_first_last_name(self):
        
        formatted_name = get_formatted_name('alex', 'wu')
        self.assertEqual(formatted_name, 'Alex Wu')

if __name__ == '__main__':
    unittest.main()