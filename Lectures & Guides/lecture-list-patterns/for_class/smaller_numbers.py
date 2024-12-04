def make_smaller(numbers):
    smaller_list = []
    for number in numbers:
        small = number / 2
        smaller_list.append(small)
    return smaller_list



if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    smaller = make_smaller(numbers)
    print(numbers)
    print(smaller)
