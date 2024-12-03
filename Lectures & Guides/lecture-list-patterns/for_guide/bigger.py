def make_bigger(numbers):
    bigger_numbers = []
    for number in numbers:
        bigger = number * 2
        bigger_numbers.append(bigger)
    return bigger_numbers


if __name__ == '__main__':
    original = [1, 2, 3, 4, 5, 6, 7, 8]
    multiplied_by_two = make_bigger(original)
    print(original)
    print(multiplied_by_two)
