def get_string():
    return input("Enter a string: ")


def main():
    print("Let’s concatenate strings!")
    while True:
        string1 = get_string()
        string2 = get_string()
        if string1 < string2:
            print(string1 + string2)
        else:
            print(f"Sorry, {string1} is greater than {string2}. I'm quitting.")
            break


if __name__ == '__main__':
    main()
