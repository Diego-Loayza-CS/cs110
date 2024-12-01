# 🍓 🍎 🥭

def get_fruit():
    return input("Select a fruit: ")


def main():
    fruits = []
    while True:
        fruit = get_fruit()
        if fruit == "q":
            break
        fruits.append(fruit)
    for fruit in fruits:
        print(f"You like {fruit}")


if __name__ == '__main__':
    main()
