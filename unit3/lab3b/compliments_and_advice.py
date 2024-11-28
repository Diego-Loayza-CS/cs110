def get_option():
    response = input("Option: ")
    return int(response)


def main():
    while True:
        print("""What would you like to do?
        1) Receive compliment
        2) Receive advice
        3) Quit""")
        option = get_option()
        if option == 1:
            print("""You write the best code!
            """)
        elif option == 2:
            print("""Get 8 hours of sleep every night.
            """)
        elif option == 3:
            print("Goodbye!")
            break



if __name__ == '__main__':
    main()
