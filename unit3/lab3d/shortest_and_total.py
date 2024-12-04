def shortest_word(words):
    shortest = None
    for word in words:
        if shortest == None or len(word) < len(shortest):
            shortest = word
    return shortest


def total_lengths(words):
    total = 0
    for word in words:
        total = total + len(word)
    return total


def main():
    words = ['the', 'elephant', 'ate', 'twenty', 'bananas', 'and', 'an', 'orange']
    shortest = shortest_word(words)
    total = total_lengths(words)
    print(f'The shortest word is: {shortest}')
    print(f'The total length of all the words is: {total}')


if __name__ == '__main__':
    main()
