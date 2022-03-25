from supermarket.models.product import Product


class ProductHandler(Product):

    def __init__(self, *args, **kwargs):
        super(ProductHandler, self).__init__(*args, **kwargs)

    def get_offer_id(self) -> int:
        return self._offer_id

    def set_offer_id(self, offerId: int) -> None:
        self._offer_id = offerId

    def get_product_name(self) -> str:
        return self._product_name

    def set_product_name(self, _productName: str):
        self._product_name = _productName

    def get_product_id(self) -> int:
        return self._product_id

    def set_product_id(self, productId: int):
        self._product_id = productId

    def get_quantity(self) -> int:
        return self._quantity

    def set_quantity(self, quantity: int):
        self._quantity = quantity

    def get_price(self) -> int:
        return self._price

    def set_price(self, price: int):
        self._price = price