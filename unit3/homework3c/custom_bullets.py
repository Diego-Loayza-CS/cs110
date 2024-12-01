def get_items():
    item_list = []
    while True:
        item = input("Item: ")
        if item == "":
            break
        item_list.append(item)
    return item_list


def get_bullet_points():
    pass


def main():
    items = get_items()
    print()
    bullet_points = get_bullet_points()


if __name__ == '__main__':
    main()
