class ProductManager:

    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})