def get_name() -> str:
    entered_name = input("What is your name? ")
    return entered_name


def get_sandwich():
    return input("What kind of sandwich do you want? ")


def get_additions():
    return input("What do you want on it? ")


def print_summary(name, sandwich, adds):
    print(f"{name} wants a {sandwich} sandwich with {adds}!")


def main():
    print("Welcome to Wendy's!")
    name = get_name()
    sandwich = get_sandwich()
    adds = get_additions()
    print_summary(name, sandwich, adds)


if __name__ == '__main__':
    main()
