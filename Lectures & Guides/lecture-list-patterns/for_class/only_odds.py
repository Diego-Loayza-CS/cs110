def only_odds(numbers):
    odds = []
    for number in numbers:
        if (number % 2) == 1:
            odds.append(number)
    return odds


if __name__ == '__main__':
    print(only_odds([1, 2, 3, 4, 5, 6]))
    
