from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        # formula for drunkenness
        # drunkenness = sum of alcohol levels of customer.body
        
    def increase_till(self, price):
        self.till += price
    
    def get_drink_by_name(self, drink_name):
        return [drink["drink"] for drink in self.drinks if drink["drink"].name == drink_name][0]

    def decrease_stock(self, drink_sold, sold_stock):
        for drink in self.drinks:
            if drink["drink"] == drink_sold:
                drink["stock"] -= sold_stock 

    def add_new_drink(self, drink, stock):
        self.drinks.append({"drink": drink, "stock": stock})

    def add_stock(self, add_drink, additional_stock):
        for drink in self.drinks:
            if drink["drink"].name == add_drink.name:
                drink["stock"] += additional_stock

    def given_drink_stock(self, given_drink):
        return sum([drink["stock"] for drink in self.drinks if drink["drink"].name == given_drink.name])

    def sell_drink(self, drink_wanted, customer, num_drinks):
        drunk_limit = 10
        for drink in self.drinks:
            if (drink["stock"] > 0) and (drink["drink"].name == drink_wanted.name) and (customer.wallet >= drink_wanted.price) and (customer.drunkenness < (drunk_limit - drink_wanted.alcoholic_status)) and (customer.age >= 18):
                self.increase_till(drink_wanted.price)
                self.decrease_stock(drink["drink"], num_drinks)
                customer.decrease_wallet(drink["drink"])
                customer.add_drink_to_body(drink["drink"])
                customer.raise_drunkenness()