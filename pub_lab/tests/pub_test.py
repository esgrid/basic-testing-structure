import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)