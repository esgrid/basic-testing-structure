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
    
    def sell_drink(self, drink_wanted, customer):
        for drink in self.drinks:
            if drink["stock"] > 0 and drink["drink"] == drink_wanted and customer.wallet >= drink_wanted.price and customer.:
                self.till += drink_wanted.price
                self.decrease_stock(drink["drink"])
                customer.decrease_wallet(drink["drink"])
                customer.add_drink_to_body(drink["drink"])