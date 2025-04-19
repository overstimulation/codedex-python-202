import unittest


class CoffeeMenu:
    def __init__(self):
        self.menu = {"espresso": 2.50, "latte": 2.75, "cappuccino": 3.20, "americano": 2.70}


class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()

    def tearDown(self):
        self.menu = None

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.menu["espresso"], 2.5)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.menu.menu["irish"]

    def test_add_item(self):
        self.menu.menu["mocha"] = 3.50
        self.assertEqual(self.menu.menu["mocha"], 3.50)


if __name__ == "__main__":
    unittest.main()
