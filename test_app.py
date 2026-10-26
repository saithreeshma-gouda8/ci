
import unittest
from app import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Saithreeshma"), "Hello, Saithreeshma!")

    def test_greet_another_name(self):
        self.assertEqual(greet("Sreeja"), "Hello, Sreeja!")

if __name__ == "__main__":
    unittest.main()
