class Sale(object):
    """ Sale products with applying offer """
    def __init__(self):
        self.__totalBill = 0

    def get_total_bill(self) -> int:
        return self.__totalBill

    def set_total_bill(self, totalBill: int) -> None:
        self.__totalBill = totalBill

    

    def sale_the_product(self, productId: int, \
        productQuantity: int, \
        inventories: dict(), \
        offers: dict() \
    ):

        def get_percentage_amount(amount: int, discount: int) -> int:
            return int(amount*(discount / 100.0))
            
        inventory = inventories[productId]
        if offers is not None and productId in offers:
            newOffer = offers[productId]
        else:
            newOffer = None
        inventory.set_quantity(inventory.get_quantity() - productQuantity)
        offer = "N/A" if inventory.get_offer_id() == -1 else str(inventory.get_offer_id())
        if newOffer is not None and \
                productQuantity >= newOffer.get_min_quantity():
            totalAmount = (productQuantity * inventory.get_price()) \
                - get_percentage_amount(
                    (productQuantity * inventory.get_price()), newOffer.get_discout_percentage())
        else:
            totalAmount = productQuantity * inventory.get_price()
        print(
            f"{inventory.get_product_id()} - {inventory.get_product_name()}"
            f" - {productQuantity}"
            f" - {inventory.get_price()}"
            f" - {offer}"
            f" - {totalAmount}"
        )

        self.set_total_bill(self.get_total_bill() + totalAmount)
