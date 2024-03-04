import unittest

from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test 'name_function.py'"""

    def test_first_last_name(self):        
        formatted_name = get_formatted_name('alex', 'wu')
        self.assertEqual(formatted_name, 'Alex Wu')

    def test_first_last_middle_name(self):
        "测试 中间名是否可以正确处理"
        formatted_name = get_formatted_name("alex", "wu", "max")
        self.assertEqual(formatted_name, "Alex Max Wu")
if __name__ == '__main__':
    unittest.main()