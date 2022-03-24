from typing import Dict
from supermarket.offers import Offers
from supermarket.product import ProductHandler
from supermarket.sale import Sale


class Shop:
    """ Shop Market to sky rocket sales """

    def __init__(self):
        # Product ID : Product Class
        self.inventories: Dict[int, ProductHandler] = dict()
        self.offers: Dict[int, Offers] = dict()


    def __add_product(self, query):
        id, name, quantity, price = query.split("|")
        self.inventories[int(id)] = ProductHandler(
            int(id), name, int(quantity), int(price))
        print("Inventory updated")

    def stock(self, query):
        product_id = int(query)
        if product_id in self.inventories:
            product = self.inventories[product_id]
            print(product)
        else:
            raise Exception(f"No product found for {product_id} id.")

    def __sale(self, query):
        print("== Bill ==")
        sales = query.split(';')
        sale = Sale()
        for product in sales:
            product_id = int(product[0])
            sold_quantity = int(product[2])
            sale.sale_the_product(
                product_id, sold_quantity, self.inventories, self.offers)
        print("== Total ==")
        print(sale.get_total_bill())
        print("========")
        sale.set_total_bill(0)

    def __add_offer(self, query):
        print("Offer Added")

    def execute(self, command):
        instruction, query = command.split("=>")

        match instruction:
            case "INVENTORY": self.__add_product(query)

            case "SALE": self.__sale(query)

            case "STOCK": self.stock(query)

            case "NEW-OFFER": self.__add_offer(query)

            case _: print("Invalid input")