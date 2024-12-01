def get_fruits():
    fruit_list = []
    while True:
        fruit = input("Enter a Fruit: ")
        if fruit == "":
            break
        fruit_list.append(fruit)
    return fruit_list


def get_vegetables():
    vegetables_list = []
    while True:
        vegetable = input("Enter a Vegetable: ")
        if vegetable == "":
            break
        vegetables_list.append(vegetable)
    return vegetables_list


def print_vegetables(vegetables):
    print("Vegetables:")
    for vegetable in vegetables:
        print(f" - {vegetable}")


def print_fruits(fruits):
    print("Fruits:")
    for fruit in fruits:
        print(f" - {fruit}")


def print_recommendation(vegetables, fruits):
    if len(vegetables) > len(fruits):
        print("You need more fruit!")
    elif len(vegetables) < len(fruits):
        print("You need more vegetables!")
    else:
        print("What a healthy balanced diet!")


def main():
    fruits = get_fruits()
    vegetables = get_vegetables()
    print_fruits(fruits)
    print_vegetables(vegetables)
    print_recommendation(vegetables, fruits)


if __name__ == '__main__':
    main()
