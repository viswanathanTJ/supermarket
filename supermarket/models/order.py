from typing import List
from models.bill_entry import BillEntry


class Order:
    def __init__(self, bill_entries: List[BillEntry]):
        self.bill_entries = bill_entries
        self.special_discount = 0
        self.combo_discount = 0
        self.total = 0
