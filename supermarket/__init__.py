class Shop:
    """ Shop Market to sky rocket sales """

    def __init__(self):
        pass

    def __add_product(self, query):
        print("Inventory updated")

    def stock(self, query):
        pass

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