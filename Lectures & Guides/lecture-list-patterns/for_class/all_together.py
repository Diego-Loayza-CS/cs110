def make_it_happen(numbers):
    subtracted_list = []
    for number in numbers:
        new_number = number - 7
        if new_number < 0:
            new_number = new_number * -1
        if new_number < 10:
            subtracted_list.append(new_number)
    return subtracted_list


if __name__ == '__main__':
    nums = [0, 7, 2, 14, 20, 32, 5, 12]
    nums = make_it_happen(nums)
    print(nums)
