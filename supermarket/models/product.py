class Product:
    """Product Details"""
    def __init__(self, product_id, product_name, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return "{} - {}".format(self.product_name, self.quantity)