from typing import Dict
from supermarket.models.product import Product


class Shop:
    """ Shop Market to sky rocket sales """

    def __init__(self):
        # Product ID : Product Class
        self.inventories: Dict[int, Product] = dict()

    def __add_product(self, query):
        id, name, quantity, price = query.split("|")
        self.inventories[int(id)] = Product(int(id), name, int(quantity), int(price))
        print("Inventory updated")

    def stock(self, query):
        product_id = int(query)
        if product_id in self.inventories:
            product = self.inventories[product_id]
            print(product)
        else:
            raise Exception(f"No product found for {product_id} id.")

    def __sale(self, query):
        pass

    def __add_offer(self, query):
        print("Offer Added")

    def execute(self, command):
        command_name, query = command.split("=>")

        match command_name:
            case "INVENTORY": self.__add_product(query)

            case "SALE": self.__sale(query)

            case "STOCK": self.stock(query)

            case "NEW-OFFER": self.__add_offer(query)

            case _: print("Invalid input")