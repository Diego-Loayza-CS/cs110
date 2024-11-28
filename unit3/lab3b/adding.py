def get_number():
    response = input("Enter a number: ")
    return int(response)


def finished_operating():
    decision = input("Would you like to do more? ")
    if decision == "no" or decision == "No":
        return True


def main():
    print("I can add numbers for you!")
    while True:
        number1 = get_number()
        number2 = get_number()
        print(f"The result is: {number1 + number2}")
        if finished_operating():
            break


if __name__ == '__main__':
    main()
