def get_numbers(prompt):
    responses = []
    while True:
        response = input(prompt)
        if response == '':
            break
        responses.append(int(response))
    return responses


def print_smaller(numbers, boundary):
    # This function should print the numbers that are smaller than the boundary
    pass


def main():
    print("Let's find you some tables and chairs!")
    total_budget = int(input("First, what is your total budget? "))

    print()
    print("Sweet! Now let me know what your table options are.")
    # 1. Get table options

    print()
    print("Next, let me know what your chair options are.")
    # 2. Get chair options

    print()
    print(f"Since your total budget is ${total_budget}, you can afford the tables that cost: ")
    # 3. Print table options

    table_cost = int(input("Which table do you want? "))
    chair_budget = total_budget - table_cost

    print()
    print(f"That means that your chair budget is ${chair_budget}.")
    print("You can afford chairs that cost: ")
    # 4. Print chair options


if __name__ == "__main__":
    main()
