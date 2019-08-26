import unittest
import types
import sympy
import src.experiment_funcs as experiment_funcs

class TestHelloWorld(unittest.TestCase):

    def test_print(self):
        self.assertEqual(experiment_funcs.hello_world(), "Hello world!")

class TestPrimes(unittest.TestCase):

    def test_edge_cases(self):
        self.assertEqual(experiment_funcs.primes(-1), [])
        self.assertEqual(experiment_funcs.primes(0), [])
        self.assertEqual(experiment_funcs.primes(1), [])
        self.assertEqual(experiment_funcs.primes(2), [2])
    
    def test_primes(self):
        self.assertEqual(experiment_funcs.primes(10), list(sympy.primerange(1, 10+1)))
        self.assertEqual(experiment_funcs.primes(11), list(sympy.primerange(1, 11+1)))
        self.assertEqual(experiment_funcs.primes(125), list(sympy.primerange(1, 125+1)))

class TestGenerator(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(experiment_funcs.generator_function(10), types.GeneratorType)
    
    def test_returns(self):
        self.assertEqual(list(experiment_funcs.generator_function(10)), list(range(10)))


if __name__ == "__main__":
    unittest.main()
