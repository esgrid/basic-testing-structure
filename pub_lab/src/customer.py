class Customer:
    def __init__(self, name, body, wallet):
        self.name = name
        self.body = body
        self.wallet = wallet
        self.drunkenness = sum([drink["drink"].alcoholic_status for drink in self.body])
        # alcohol level allowed = 10

    def buy_drink(self, drink):
        self.wallet -= drink.price