def double_words(words):
    double_list = []
    for word in words:
        doubled = word + " " + word
        double_list.append(doubled)
    return double_list


def print_words(words):
    for word in words:
        print(f"- {word}")


def main():
    words = ['really', 'very', 'so', 'crazy']
    doubled = double_words(words)
    print_words(doubled)


if __name__ == '__main__':
    main()
