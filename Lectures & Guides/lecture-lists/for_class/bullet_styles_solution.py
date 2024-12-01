def get_items():
    """
    Prompt the user for items until they provide 'q'
    Return the items in a list
    """
    items = []
    while True:
        item = input('Item: ')
        if item == '':
            break
        items.append(item)

    return items


def print_items(items, bullet):
    for item in items:
        print(f'{bullet} {item}')
    print()

    
def main():
    items = get_items()
    print_items(items, '*')
    print_items(items, '-')
    print_items(items, '>')


if __name__ == '__main__':
    main()
    
