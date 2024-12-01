# :)

def main():
    item_list = []
    while True:
        item = input("Select an item: ")
        if item == "q":
            break
        item_list.append(item)
    return item_list


def print_list(items, param):
    for item in items:
        print(f"{param} {item}")
    print()


if __name__ == '__main__':
    items = main()
    print_list(items, "*")
    print_list(items, "-")
    print_list(items, ">")
