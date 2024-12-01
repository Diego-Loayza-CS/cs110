def get_numbers():
    numbers = []
    while True:
        response = input('Number: ')
        if response == '':
            break
        
        number = int(response)
        numbers.append(number)
        
    return numbers
    
    
def get_bound():
    return int(input('Boundary: '))


def print_numbers(numbers, bound):
    for number in numbers:
        if number < bound:
            big_or_small = 'small'
        else:
            big_or_small = 'big'
        print(f'- {number} ({big_or_small})')
                        

def main():
    numbers = get_numbers()
    bound = get_bound()
    print(f'You have {len(numbers)} numbers:')
    print_numbers(numbers, bound)
    

if __name__ == '__main__':
    main()
    
