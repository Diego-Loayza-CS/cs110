def play(secret_number):
    while True:
        response = int(input('Guess a number: '))

        if response > secret_number:
            print('Lower!')

        elif response < secret_number:
            print('Higher!')

        else:
            print('You got it!')
            return


if __name__ == '__main__':
    play(37)
