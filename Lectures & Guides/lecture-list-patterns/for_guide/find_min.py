def find_min(numbers):
    smallest = None
    for number in numbers:
        if smallest is None or number < smallest:
            smallest = number
    return smallest


if __name__ == '__main__':
    print(find_min([3, 6, 2, 8, 1, 7]))
    
