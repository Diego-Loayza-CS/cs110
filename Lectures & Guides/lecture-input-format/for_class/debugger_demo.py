def get_name():
    name = input('Hello, what is your name? ')
    return name
    
    
def get_age():
    age = input('And what is your age? ')
    return age


def print_message(name, age):
    print(f'{age} years ago, {name} was born!')

    
def main():
    name = get_name()
    age = get_age()
    print_message(name, age)
    
    
if __name__ == '__main__':
    main()
    
