import math
import unittest


class TestUnexpected(unittest.TestCase):
    def test_sqrt_result(self):
        result = get_sqrt(144)
        self.assertEqual(result, 12)

    def test_sqrt_value(self):
        with self.assertRaises(ValueError):
            get_sqrt(-1)

    def test_divide_result(self):
        result = divide(5, 2)
        self.assertEqual(result, 2.5)

    def test_divide_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


def get_sqrt(n):
    return math.sqrt(n)


def divide(a, b):
    return a / b


if __name__ == "__main__":
    unittest.main()
