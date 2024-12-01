def get_items():
    item_list = []
    while True:
        item = input("Item: ")
        if item == "":
            break
        item_list.append(item)
    return item_list


def get_bullet_points():
    bullet_list = []
    while True:
        bullet = input("Custom Bullet Point: ")
        if bullet == "":
            break
        bullet_list.append(bullet)
    return bullet_list


def print_lists(items, bullet_points):
    for bullet in bullet_points:
        for item in items:
            print(f"{bullet} {item}")
        print()


def main():
    items = get_items()
    print()
    bullet_points = get_bullet_points()
    print()
    print_lists(items, bullet_points)


if __name__ == '__main__':
    main()
