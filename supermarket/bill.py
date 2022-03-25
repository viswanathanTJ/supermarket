from typing import List
from supermarket.models.bill_entry import BillEntry

class Bill:
    def __init__(self, bill_entries: List[BillEntry]):
        self.bill_entries = bill_entries
        self.total = 0

    def get_total(self):
        total = 0
        for entry in self.bill_entries:
            total += entry.net_price
        total -= self.special_discount
        self.total = total

    def set_total(self, total):
        self.total = total

    def __str__(self):
        print("== Bill ==")
        for entry in self.bill_entries:
            print("{} - {} - {} - {} - {} - {}".format(entry.product_id, entry.product_name,
                  entry.quantity, entry.product_price, entry.offer_id, entry.net_price))
        print("== Total ==")
        print(self.total)
        print("============")
        return ""
