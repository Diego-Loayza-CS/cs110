if __name__ == '__main__':
    names = []
    while True:
        name = input("Give me a name: ")
        if name == 'q':
            break
        names.append(name)

    print(names)