from typing import List
from supermarket.bill import Bill
from supermarket.models.bill_entry import BillEntry

class Sale(object):
    """ Sale products with applying offer """
    def __init__(self):
        self.__totalBill = 0
        self.bill_entries: List[BillEntry] = []

    def get_total_bill(self) -> int:
        return self.__totalBill

    def set_total_bill(self, totalBill: int) -> None:
        self.__totalBill = totalBill

    def sale_the_product(self, query):
        self.bill_entries = []
        from supermarket import inventories

        for prod in query.split(";"):
            product_id = int(prod[0])
            sold_quantity = int(prod[2])
            
            if product_id not in inventories:
                raise Exception("Product not found in inventory")
            product = inventories[product_id]

            price = product._price*sold_quantity

            self.bill_entries.append(BillEntry(
                product_id, product._product_name, sold_quantity, product._price, "N/A", price))
        
        order = Bill(self.bill_entries)
        print(order)

    def __str__(self):
        return ""