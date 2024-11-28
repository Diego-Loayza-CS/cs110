def main():
    while True:
        # Display menu
        print()
        print('What would you like to do?')
        print(' 1) Receive compliment')
        print(' 2) Receive advice')
        print(' 3) Quit')
        
        # Get response
        response = input('Option: ')
        
        # Take action
        if response == '1':
            print("Your nose looks very nice.")
            
        elif response == '2':
            print("Get more sleep.")
            
        elif response == '3':
            print('Good bye!')
            return
        
        else:
            print(f"Unrecognized response: {response}")


if __name__ == '__main__':
    main()
    
