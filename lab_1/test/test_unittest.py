import unittest, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import calculator as calc


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)

    def test_square_root(self):
        self.assertEqual(calc.square_root(4), 2)

if __name__ == '__main__':
    unittest.main()