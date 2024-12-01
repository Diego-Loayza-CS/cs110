def get_adjectives():
    adjective_list = []
    while True:
        adjective = input("Enter an adjective: ")
        if adjective == "":
            break
        adjective_list.append(adjective)
    return adjective_list


def get_verbs():
    verb_list = []
    while True:
        verb = input("""Enter a verb ending in "ing": """)
        if verb == "":
            break
        verb_list.append(verb)
    return verb_list


def print_actions(adjectives, verbs):
    for adjective in adjectives:
        print(f"The puppy is {adjective}!")
    for verb in verbs:
        print(f"The puppy is {verb}!")
    print("The puppy is taking a nap.")


def main():
    adjectives = get_adjectives()
    verbs = get_verbs()
    print_actions(adjectives, verbs)


if __name__ == '__main__':
    main()
