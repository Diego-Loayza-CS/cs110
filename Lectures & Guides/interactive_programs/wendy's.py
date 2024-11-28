def get_name():
    return input("What is your name? ")


def get_type():
    return input("What kind of sandwich do you want? ")


def get_additions():
    return input("What do you want on it? ")


def print_order():
    print(f"{name} wants a {type} sandwich with {additions}!")


if __name__ == '__main__':
    print("Welcome to Wendy's")
    name = get_name()
    type = get_type()
    additions = get_additions()
    print_order()
