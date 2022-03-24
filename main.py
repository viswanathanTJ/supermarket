
from supermarket import Shop

if __name__ == "__main__":
    my_shop = Shop()
    while(True):
        try:
            command = input()
            if command.lower() == "exit":
                break
            my_shop.execute(command)
        except KeyboardInterrupt:
            break
        except Exception as err:
            print("Error:", err)