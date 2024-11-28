def print_introduction():
    print("Welcome to Papa John's!")


def get_name():
    return input("What is your name? ")


def get_kind():
    return input("What kind of pizza do you want? ")


def get_topping():
    return input("What toppings do you want? ")


def print_order(name, kind, topping):
    print(f"{name} wants a {kind} pizza with {topping}!")


def pizza_time():
    print_introduction()
    name = get_name()
    kind = get_kind()
    topping = get_topping()
    print_order(name, kind, topping)


if __name__ == '__main__':
    pizza_time()
