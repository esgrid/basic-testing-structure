import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_sell_drink(self):
        drink = Drink("Drink 1", 10, 5)
        customer = Customer("José Pablo", [], 100.00)
        self.pub.sell_drink(drink, customer)
        self.assertEqual(self.pub.drinks[0]["stock"], 0)
        

    def test_pub_acquire_drink(self):
        pass

    def test_pub_increase_till(self):
        pass

    def test_pub_drink_stock(self):
        pass