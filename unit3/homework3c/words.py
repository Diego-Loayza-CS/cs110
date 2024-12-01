def get_words():
    word_list = []
    while True:
        word = input("Word: ")
        if word == "":
            break
        word_list.append(word)
    return word_list


def order_words(words, boundary):
    print("These are small:")
    for word in words:
        if word < boundary:
            print(f"{word}")
    print("These are big:")
    for word in words:
        if word > boundary:
            print(f"{word}")


def main():
    words = get_words()
    boundary = input("Boundary: ")
    print(f"You have {len(words)} words")
    order_words(words, boundary)


if __name__ == '__main__':
    main()
