def get_items():
    items = []
    while True:
        response = input('Enter an item: ')
        if response == '':
            break
        items.append(response)

    return items


def main():
    shopping_list = get_items()
    print(shopping_list)


if __name__ == '__main__':
    main()
