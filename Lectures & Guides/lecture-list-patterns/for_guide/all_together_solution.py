def should_keep(number):
    return number >= 0 and number <= 10


def filter_numbers(numbers):
    new = []
    for number in numbers:
        if should_keep(number):
            new.append(number)
    return new


def sub_7(numbers):
    new = []
    for number in numbers:
        new.append(number - 7)
    return new


def make_it_happen(numbers):
    numbers = sub_7(numbers)
    numbers = filter_numbers(numbers)
    return numbers


if __name__ == '__main__':
    nums = [0, 7, 2, 14, 20, 32, 5, 12]
    nums = make_it_happen(nums)
    print(nums)
    
