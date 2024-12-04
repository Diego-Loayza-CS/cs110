def get_words():
    word_list = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        word_list.append(word)
    return word_list


def get_length():
    return int(input("Enter a length: "))


def select_short_words(words, max_length):
    short_list = []
    for word in words:
        if len(word) <= max_length:
            short_list.append(word)
    return short_list


def print_short_words(final_list):
    print(f"There are {len(final_list)} short words:")
    for word in final_list:
        print(f"- {word}")

def main():
    words = get_words()
    max_length = get_length()
    final_list = select_short_words(words, max_length)
    print_short_words(final_list)


if __name__ == '__main__':
    main()
