def get_number():
    response = input("Enter a number: ")
    return int(response)


def main():
    number1 = get_number()
    number2 = get_number()

    if number1 > number2:
        print(f"{number1} is bigger than {number2}")
        
    elif number1 < number2:
        print(f"{number1} is smaller than {number2}")
        
    else:
        print(f"You entered {number1} twice.")
        
        
if __name__ == '__main__':
    main()
    
