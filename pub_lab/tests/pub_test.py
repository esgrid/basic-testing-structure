import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Drink 1", 10, 5)
        self.drink2 = Drink("Drink 2", 10, 4)
        self.drink3 = Drink("Drink 3", 3, 1)
        self.drink4 = Drink("Drink 4", 4, 4)
        self.drink5 = Drink("Drink 5", 2, 2)
        self.drinks = [
                        {"drink": self.drink1, "stock": 1}, 
                        {"drink": self.drink2, "stock": 2}, 
                        {"drink": self.drink3, "stock": 1}, 
                        {"drink": self.drink4, "stock": 3}, 
                        {"drink": self.drink5, "stock": 0}
                    ]
        self.pub = Pub("The Prancing Pony", 100.00, self.drinks)

    # @unittest.skip("Delete or comment to run test")
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        
    # @unittest.skip("Delete or comment to run test")
    def test_pub_acquire_drink(self):
        self.pub.add_new_drink(Drink("Drink 6", 15, 6), 5)
        self.assertEqual("Drink 6s5", self.pub.drinks[5]["drink"].name + "s" + str(self.pub.drinks[5]["stock"]))

    # @unittest.skip("Delete or comment to run")
    def test_pub_increase_till(self):
        self.pub.increase_till(self.drinks[1]["drink"].price)
        self.assertEqual(110, self.pub.till)

    # @unittest.skip("Delete or comment to run test")
    def test_pub_add_stock(self):
        self.pub.add_stock(self.drink5, 3)
        self.assertEqual(3, self.pub.drinks[4]["stock"])

    def test_decrease_stock(self):
        self.pub.decrease_stock(self.drink2, 1)
        self.assertEqual(1, self.pub.drinks[1]["stock"])

    # @unittest.skip("Delete or comment to run test")
    def test_pub_drink_stock(self):
        self.pub.add_stock(self.drink5, 2)
        self.assertEqual(2, self.pub.given_drink_stock(self.drink5))

    # @unittest.skip("Delete or comment to run test")
    def test_get_drink_by_name(self):
        self.assertEqual("Drink 4", self.pub.get_drink_by_name("Drink 4").name)

    def test_all_stock_value(self):
        total_value = sum([drink["stock"]*drink["drink"].price for drink in self.drinks])
        total_value -= self.drink5.price*1
        self.pub.decrease_stock(self.drink5, 1)
        self.assertEqual(total_value, self.pub.total_stock_value())

    # @unittest.skip("Delete or comment to run test")
    def test_pub_sell_drink(self):
        customer = Customer("José Pablo", [], 100.00, 18)
        self.pub.sell_drink(self.drink1, customer, 1)
        self.assertEqual(0, self.pub.drinks[0]["stock"])
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(self.drink1.name, customer.body[0].name)
        self.assertEqual(90, customer.wallet)
        self.assertEqual(5, customer.drunkenness)

    def test_pub_sell_food(self):
        food = Food("Food 1", 10, 3)
        customer = Customer("José Pablo", [], 100.00, 18)
        
        self.pub.sell_drink(self.drink2, customer, 1)
        self.pub.sell_food(food, customer)
        self.assertEqual(80, customer.wallet)
        self.assertEqual(1, customer.drunkenness)