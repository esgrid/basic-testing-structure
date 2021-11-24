from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink1 = Drink("Drink 1", 5, 2)
        self.drink2 = Drink("Drink 2", 10, 4)
        self.drink3 = Drink("Drink 3", 3, 1)
        self.drinks = [self.drink1, self.drink2, self.drink3, self.drink4, self.drink5]