from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
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
        # formula for drunkenness
        # drunkenness = sum of alcohol levels of customer.body
    def decrease_stock(self, drink_sold):
        for drink in self.drinks:
            if drink["drink"] == drink_sold:
                drink["stock"] -=1 

    def add_new_drink(self,drink, stock):
        self.drinks.append({"drink": drink, "stock": stock})

    def add_stock(self, add_drink, additional_stock):
        for drink in self.drinks:
            if drink["drink"] == add_drink:
                drink["stock"] += additional_stock

    def sell_drink(self, drink_wanted, customer):
        drunk_limit = 10
        for drink in self.drinks:
            if drink["stock"] > 0 and drink["drink"] == drink_wanted and customer.wallet >= drink_wanted.price and customer.drunkenness < drunk_limit - drink_wanted.alcoholic_status:
                self.till += drink_wanted.price
                self.decrease_stock(drink["drink"])
                customer.buy_drink(drink["drink"])
                customer.decrease_wallet(drink["drink"])
                customer.add_drink_to_body(drink["drink"])
                customer.raise_drunkenness()