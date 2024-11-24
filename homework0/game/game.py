import random


def get_a_guess(player):
    while True:
        guess = input(f"{player}, enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            break
        print("I need you to enter a number.")

    return guess


def get_guesses(player1, player2):
    # instructions
    print("I have picked a random number between 1 and 100.")
    print("Can you guess it?")
    print()

    # get guesses
    guess1 = get_a_guess(player1)
    guess2 = get_a_guess(player2)

    return guess1, guess2


def determine_winner(number, player1, player2, guess1, guess2):
    # get differences
    diff1 = abs(number - guess1)
    diff2 = abs(number - guess2)

    # determine winner
    if diff1 == diff2:
        if diff1 == 0:
            print("Wow, you both guessed it!")
        else:
            print(f"You tied! The number was {number} and you were both {diff1} away.")

    elif diff1 < diff2:
        if diff1 == 0:
            print(f"Wow, {player1}, you guessed it exactly. You win!")
        else:
            print(f"{player1} wins! The number was {number} and {player1} was {diff1} away.")
        print(f"Sorry, {player2}, you were {diff2} away.")

    else:
        if diff2 == 0:
            print(f"Wow, {player2}, you guessed it exactly. You win!")

        else:
            print(f"{player2} wins! The number was {number} and {player2} was {diff2} away.")
        print(f"Sorry, {player1}, you were {diff1} away.")


def main():
    # get names
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # pick a number
    number = random.randint(1, 100)

    # get guesses
    guess1, guess2 = get_guesses(player1, player2)

    determine_winner(number, player1, player2, guess1, guess2)


if __name__ == '__main__':
    main()




