def get_list(prompt):
    responses = []
    while True:
        response = input(prompt)
        if response == '':
            break
        responses.append(response)
    return responses


def print_list(header, items, bullet):
    print(header)
    for item in items:
        print(f'{bullet} {item}')


def main():
    # Write code here
    visited = get_list("Enter a place you have visited: ")
    want_to_visit = get_list("Enter a place you want to visit: ")
    print_list("I have visited ", visited, "- ")
    print_list("I want to visit ", want_to_visit, "- ")


if __name__ == '__main__':
    main()
