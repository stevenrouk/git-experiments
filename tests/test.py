# Importing main.py this way, per Real Python recommendation:
# https://realpython.com/python-testing/
main_py = __import__("../src/main.py")

import unittest

class TestHelloWorld(unittest.TestCase):

    def test_print(self):
        self.assertEqual(main_py.hello_world(), "Hello world!")

if __name__ == "__main__":
    unittest.main()
