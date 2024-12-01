# Have fun!

def get_numbers():
    num_list = []
    while True:
        number = input("Number: ")
        if number == "":
            break
        num_list.append(int(number))
    return num_list


def show_numbers(numbers, boundary):
    print(f"You have {len(numbers)} numbers:")
    for number in numbers:
        if number < boundary:
            print(f"- {number} (small)")
        elif number > boundary:
            print(f"- {number} (big)")
        else:
            print(f"- {number} (boundary)")


def main():
    numbers = get_numbers()
    boundary = int(input("Boundary: "))
    show_numbers(numbers, boundary)


if __name__ == '__main__':
    main()
