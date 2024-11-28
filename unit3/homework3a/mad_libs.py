def print_introduction():
    print("""Welcome to Mad Libs!
Please enter the following words:""")


def get_noun():
    return input("Noun: ")


def get_adjective():
    return input("Adjective: ")


def get_number():
    return input("Number: ")


def get_past_tense_verb():
    return input("Past-Tense Verb: ")


def get_game():
    return input("Game: ")


def get_verb():
    return input("Verb: ")


def print_story(noun1, adjective1, adjective2, noun2, number, adjective3, past_tense_verb, game, verb):
    print(f"""Once upon a time a student at found themselves in a {noun1} class.
The teacher was so {adjective1} that the student started to daydream about a {noun2}.
Then the student woke up and realized that they were still in class.
The teacher was so {adjective2} that they gave the student a {number} on the assignment.
The student was so {adjective3} that he {past_tense_verb} the class and went home to play {game}.
The moral of the story is that you should never {verb} in class.""")


def mad_libs():
    print_introduction()
    noun1 = get_noun()
    adjective1 = get_adjective()
    adjective2 = get_adjective()
    noun2 = get_noun()
    number = get_number()
    adjective3 = get_adjective()
    past_tense_verb = get_past_tense_verb()
    game = get_game()
    verb = get_verb()
    print_story(noun1, adjective1, adjective2, noun2, number, adjective3, past_tense_verb, game, verb)


if __name__ == '__main__':
    mad_libs()
