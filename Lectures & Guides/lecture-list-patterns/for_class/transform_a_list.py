def make_bigger(numbers):
    bigger_numbers = []
    for number in numbers:
        bigger = number * 2
        bigger_numbers.append(bigger)
    return bigger_numbers


if __name__ == '__main__':
    a_few_ints = [1, 2, 3, 4, 5, 6, 7, 8]
    bigger = make_bigger(a_few_ints)
    print(a_few_ints)
    print(bigger)
