def average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


if __name__ == '__main__':
    print(average([1, 2, 3, 4]))