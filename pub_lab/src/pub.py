# from src.drink import Drink
# from src.customer import Customer

class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.max_drunk_level = 20
        # formula for drunkenness
        # drunkenness = sum of alcohol levels of customer.body
        
    def increase_till(self, price):
        self.till += price
    
    def get_drink_by_name(self, drink_name):
        return [drink["drink"] for drink in self.drinks if drink["drink"].name == drink_name][0]

    def decrease_stock(self, drink_sold, sold_stock):
        for drink in self.drinks:
            if drink["drink"].name == drink_sold.name:
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
        for drink in self.drinks:
            if (drink["stock"] > 0) and (drink["drink"].name == drink_wanted.name) and (customer.wallet >= drink_wanted.price) and (customer.drunkenness < (self.max_drunk_level - drink_wanted.alcoholic_status)) and (customer.age >= 18):
                self.increase_till(drink_wanted.price)
                self.decrease_stock(drink["drink"], num_drinks)
                customer.decrease_wallet(drink["drink"].price)
                customer.add_drink_to_body(drink["drink"])
                customer.raise_drunkenness()
    
    def total_stock_value(self):
        return sum([drink["stock"]*drink["drink"].price for drink in self.drinks])

    def sell_food(self, food, customer):
        customer.decrease_wallet(food.price)
        self.increase_till(food.price)
        customer.drunkenness = 0 if customer.drunkenness <= food.dedrunkenness_level else customer.decrease_drunkenness(food.dedrunkenness_level)
