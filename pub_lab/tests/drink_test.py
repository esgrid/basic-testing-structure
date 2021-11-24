import unittest
from src.drink import Drink
from src.drink import Drink
from src.customer import Customer

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Edinburgh Beer", 8.00, 2)

    
    # def test_drink_has_name(self):
    #     self.assertEqual("Edinburgh Beer", self.drink.name)