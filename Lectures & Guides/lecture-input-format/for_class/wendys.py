def get_name():
    return input("What is your name? ")


def get_sandwich():
    return input("What kind of sandwich do you want? ")


def get_extras():
    return input("What do you want on it? ")


def print_order(name, type, extras):
    print(f"{name} wants a {type} sandwich with {extras}!")


if __name__ == '__main__':
    print("Welcome to Wendy's!")
    name = get_name()
    type = get_sandwich()
    extras = get_extras()
    print_order(name, type, extras)
