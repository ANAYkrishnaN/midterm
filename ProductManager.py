class ProductManager:

    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})

    # This method calculates discount price for a product
    def calculateDiscount(self, price, discount_percent):
        return price - (price * discount_percent / 100)
        # temporary feature branch test