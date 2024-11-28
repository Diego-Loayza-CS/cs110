def play(secret_word):
    while True:
        guess = input("Guess a word: ")
        if guess < secret_word:
            print("Higher!")
        elif guess > secret_word:
            print("Lower!")
        else:
            print("You got it!")
            break


if __name__ == '__main__':
    secret_word = input('Enter a secret word: ')
    play(secret_word)
