import unittest
from my_project.string_utils import to_uppercase, reverse_string

class TestStringUtils(unittest.TestCase):
    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase(""), "")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

if __name__ == "__main__":
    unittest.main()