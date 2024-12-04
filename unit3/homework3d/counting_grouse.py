def get_counts():
    count_list = []
    while True:
        count = input("Enter an observation count: ")
        if count == "":
            break
        count_list.append(int(count))
    return count_list


def get_smallest(observation_count):
    smallest = None
    for count in observation_count:
        if smallest is None or smallest > count:
            smallest = count
    return smallest


def get_largest(observation_count):
    largest = None
    for count in observation_count:
        if largest is None or largest < count:
            largest = count
    return largest


def print_details(observation_count):
    total = sum(observation_count)
    smallest = get_smallest(observation_count)
    largest = get_largest(observation_count)
    print(f"There are {total} total grouse.")
    print(f"The smallest count is: {smallest}")
    print(f"The largest count is: {largest}")


def estimate(observation_count, factor):
    new_count_list = []
    for count in observation_count:
        new_count = count * factor
        new_count_list.append(new_count)
    return new_count_list


def print_estimation(estimated_population):
    print("The estimated grouse populations are:")
    for count in estimated_population:
        print(f"- {count}")


def main():
    observation_count = get_counts()
    print_details(observation_count)
    factor = int(input("Enter factor: "))
    estimated_population = estimate(observation_count, factor)
    print_estimation(estimated_population)


if __name__ == '__main__':
    main()
