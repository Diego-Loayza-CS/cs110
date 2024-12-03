def make_smaller(numbers):    
    smaller_numbers = []
    for number in numbers:
        smaller = number // 2
        smaller_numbers.append(smaller)
    return smaller_numbers


if __name__ == '__main__':
    original = [1, 2, 3, 4, 5, 6, 7, 8]
    divided_by_two = make_smaller(original)
    print(original)
    print(divided_by_two)
