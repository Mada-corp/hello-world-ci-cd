# test_app.py
import unittest
from app import create_app

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(create_app().hello_world(), "Hello, World!")   

if __name__ == '__main__':
    unittest.main()
