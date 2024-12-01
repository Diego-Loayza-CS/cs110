def get_numbers():
    numbers = []
    while True:
        response = input('Number: ')
        if response == 'q':
            break
        
        number = int(response)
        numbers.append(number)
        
    return numbers
    
    
def get_bound():
    return int(input('Boundary: '))


def print_length(numbers):
    print(f'You have {len(numbers)} numbers')


def print_small(numbers, bound):
    print('These are small:')
    for number in numbers:
        if number < bound:
            print(number)
            

def print_big(numbers, bound):
    print('These are big:')
    for number in numbers:
        if number >= bound:
            print(number)
            

def main():
    numbers = get_numbers()
    bound = get_bound()
    print_length(numbers)
    print_small(numbers, bound)
    print_big(numbers, bound)
    

if __name__ == '__main__':
    main()
    
