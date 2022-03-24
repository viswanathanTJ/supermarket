class Product:
    """Product Details"""
    def __init__(self, product_id, product_name, quantity, price):
        self._product_id = product_id
        self._product_name = product_name
        self._quantity = quantity
        self._price = price
        self._offer_id = -1

    def __str__(self):
        return "{} - {}".format(self._product_name, self._quantity)