import unittest


class MyTestCase(unittest.TestCase):
    def test_reverse_string(self):
        result = reverse_string("Kacper")
        self.assertEqual(result, "repcaK")

    def test_capitalize_string(self):
        result = capitalize_string("world")
        self.assertEqual(result, "World")

    def test_is_capitalized(self):
        result = is_capitalized("hello")
        self.assertFalse(result)


def reverse_string(s):
    return s[::-1]


def capitalize_string(s):
    return s.capitalize()


def is_capitalized(s):
    return s[0].isupper()


if __name__ == "__main__":
    unittest.main()
