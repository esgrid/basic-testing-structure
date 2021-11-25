class Customer:
    def __init__(self, name, body, wallet, age):
        self.name = name
        self.body = body
        self.wallet = wallet
        self.drunkenness = 0
        self.age = age
        # alcohol level allowed = 10

    def add_drink_to_body(self, drink):
        self.body.append(drink)
    
    def decrease_wallet(self, drink):
        self.wallet -= drink.price

    def raise_drunkenness(self):
        self.drunkenness = sum([drink.alcoholic_status for drink in self.body])