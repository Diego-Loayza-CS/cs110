def choose():
    return input('Choice: ')


def bad_choice():
    print("I didn't understand that option.")
    
    
def go_left():
    print('You go left.')
    print('You found a rock!')
    return 'a rock'


def go_right(item):
    print('You go right.')
    print('You see an ugly ogre guarding a diamond.')
    if item == 'a rock':
        print('You have a rock, so you hit the ogre with the rock and take a diamond.')
        return 'a diamond'
    
    else:
        print(f'You have {item}, so you leave.')
        return item
        
    
def enter_cave():
    print('You entered the cave.')
    item = 'nothing'
    
    while True:
        print('You can go [left] or [right] (or [leave]).')
        response = choose()
        if response == 'left':
            item = go_left()
        
        elif response == 'right':
            item = go_right(item)
           
        elif response == 'leave':
            if item == 'nothing':
                print("But you haven't found anything yet. Keep looking!")
            else:
                return item
            
        else:
            bad_choice()

            
def go_on_adventure():
    while True:
        print('You found a cave!')
        print('1) Go in it')
        print('2) Go home')
        response = choose()
    
        if response == '1':
            return enter_cave()

        elif response == '2':
            print("No! That's lame. You haven't found anything yet.")

        else:
            bad_choice()
        
        
def main():
    item = go_on_adventure()
    print(f'You returned victoriously with {item}!')


if __name__ == '__main__':
    main()
    
