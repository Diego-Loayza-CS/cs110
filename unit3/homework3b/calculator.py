def get_number1():
    response = input("Number 1: ")
    return int(response)


def get_number2():
    response = input("Number 2: ")
    return int(response)


def print_options():
    print("""
    What would you like to do?
     1) Add
     2) Subtract
     3) Quit""")


def calculator():
    while True:
        print_options()
        option = int(input("Option: "))
        if option == 1:
            number1 = get_number1()
            number2 = get_number2()
            print(f"{number1 + number2}")
        elif option == 2:
            number1 = get_number1()
            number2 = get_number2()
            print(f"{number1 - number2}")
        elif option == 3:
            return
        else:
            print(f"Unrecognized response: {option}")


if __name__ == '__main__':
    calculator()
