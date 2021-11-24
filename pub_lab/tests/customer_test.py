import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Juan Pérez", [], 100.00)

    
    # def test_pub_has_name(self):
    #     self.assertEqual("The Prancing Pony", self.pub.name)