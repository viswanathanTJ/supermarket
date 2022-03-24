class ProductOffer(object):
    def __init__(self, offer_id: int , product_id: int, min_quantity: int, discount_percent: int):
        self._offer_id = offer_id
        self._product_id = product_id
        self._min_quantity = min_quantity
        self._discount_percent = discount_percent
