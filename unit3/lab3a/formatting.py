def print_sentence(noun, verb1, verb2, adverb, noun2):
    print (f"The {noun} {verb1} and {verb2} {adverb}, so he won first prize -- a {noun2}.")


def main():
    noun = 'dog'
    verb1 = 'jumped'
    verb2 = 'danced'
    adverb = 'gracefully'
    noun2 = 'fish stick'
    print_sentence(noun, verb1, verb2, adverb, noun2)


if __name__ == '__main__':
    main()
