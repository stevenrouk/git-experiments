import unittest

import src.experiment_funcs as experiment_funcs

class TestHelloWorld(unittest.TestCase):

    def test_print(self):
        self.assertEqual(experiment_funcs.hello_world(), "Hello world!")

if __name__ == "__main__":
    unittest.main()
