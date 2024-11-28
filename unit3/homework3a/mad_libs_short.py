def print_welcome():
    print("""Welcome to Mad Libs!
Please enter the following words:""")


def get_noun():
    return input("Noun: ")


def get_adjective():
    return input("Adjective: ")


def get_character():
    return input("Character: ")


def get_animal():
    return input("Animal (Plural): ")


def print_story(noun1, adjective, noun2, character, animal):
    print(f"""{noun1} sat on a {noun2}.
{noun1} had a {adjective} fall.
All {character}'s {animal} and all the {character}'s men couldn't put {noun1} together again.""")


def mad_libs_short():
    print_welcome()
    noun1 = get_noun()
    adjective = get_adjective()
    noun2 = get_noun()
    character = get_character()
    animal = get_animal()
    print_story(noun1, adjective, noun2, character, animal)


if __name__ == '__main__':
    mad_libs_short()
