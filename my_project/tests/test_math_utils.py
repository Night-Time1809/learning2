import unittest
from my_project.math_utils import add_numbers, multiply_numbers

class TestMathUtils(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(3, 5), 15)
        self.assertEqual(multiply_numbers(0, 10), 0)

if __name__ == "__main__":
    unittest.main()