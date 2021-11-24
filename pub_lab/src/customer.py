class Customer:
    def __init__(self, name, body, wallet):
        self.name = name
        self.body = body
        self.wallet = wallet
        self.drunkenness = 0
        # alcohol level allowed = 10

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def add_drink_to_body(self, drink):
        self.body.append(drink)
    
    def decrease_wallet(self, drink):
        self.wallet -= drink.price

    def raise_drunkenness(self):
        self.drunkenness = sum([drink["drink"].alcoholic_status for drink in self.body])
