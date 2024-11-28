def get_number():
    picked_number = input("Pick a number: ")
    return int(picked_number)

def play(secret_number):
    number = get_number()
    if number > secret_number:
        print()


if __name__ == '__main__':
    play(21)
    
