def print_welcome():
    print("""Hi! This is a remembering tool.
Here, you can type three ideas you'd like to remember in the future:
""")


def get_idea1():
    return input("Write here your first idea: ")


def get_idea2():
    return input("Now your second idea: ")


def get_idea3():
    return input("Last but not least, your third idea: ")


def print_gratitude():
    print("Thank you very much! This is what you asked to remember:")


def print_ideas(idea1, idea2, idea3):
    print(f"""First idea: {idea1}
Second idea: {idea2}
Third idea: {idea3}
""")


def print_goodbye():
    print("See you next time!")


def main():
    print_welcome()
    idea1 = get_idea1()
    idea2 = get_idea2()
    idea3 = get_idea3()
    print_gratitude()
    print_ideas(idea1, idea2, idea3)
    print_goodbye()


if __name__ == '__main__':
    main()
