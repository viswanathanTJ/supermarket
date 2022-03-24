from supermarket import Shop

def start_shop():
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

if __name__ == "__main__":
    start_shop()