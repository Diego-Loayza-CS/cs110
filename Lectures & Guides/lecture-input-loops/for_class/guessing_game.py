def get_number():
    picked_number = input("Pick a number: ")
    return int(picked_number)


def play(secret_number):
    while True:
        number = get_number()
        if number > secret_number:
            print("Lower")
        elif number < secret_number:
            print("Higher")
        else:
            print("Congratulations! You guessed the number")
            break


if __name__ == '__main__':
    play(21)
