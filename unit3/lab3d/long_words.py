def long_words(words):
    long_list = []
    for word in words:
        if len(word) > 5:
            long_list.append(word)
    return long_list


def print_words(words):
    for word in words:
        print(f"- {word}")


def main():
    words = ['completely', 'fun', 'program', 'to', 'write', 'hahaha']
    long = long_words(words)
    print_words(long)


if __name__ == '__main__':
    main()
