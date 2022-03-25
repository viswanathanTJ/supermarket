from typing import Dict
from supermarket.bill import Bill
from supermarket.offers import Offers
from supermarket.product import ProductHandler
from supermarket.sale import Sale


inventories: Dict[int, ProductHandler] = dict()
offers: Dict[int, Offers] = dict()

class Shop:
    """ Shop Market to sky rocket sales """

    def __init__(self):
        pass


    def __add_product(self, query):
        id, name, quantity, price = query.split("|")
        inventories[int(id)] = ProductHandler(
            int(id), name, int(quantity), int(price))
        print("Inventory updated")

    def stock(self, query):
        product_id = int(query)
        if product_id in inventories:
            product = inventories[product_id]
            print(product)
        else:
            raise Exception(f"No product found for {product_id} id.")

    def __sale(self, query):
        # pass
        sale = Sale()
        sale.sale_the_product(query)

        

    def __add_offer(self, query):
        print("Offer Added")

    def execute(self, command):
        instruction, query = command.split("=>")

        if instruction == "INVENTORY": 
            self.__add_product(query)

        elif instruction == "SALE": 
            self.__sale(query)

        elif instruction == "STOCK": 
            self.stock(query)

        elif instruction == "NEW-OFFER": 
            self.__add_offer(query)

        else: print("Invalid input")