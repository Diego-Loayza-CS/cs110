def get_fruits():
    fruits = []
    while True:
        fruit = input('Fruit: ')
        if fruit == '':
            return fruits
        fruits.append(fruit)
    
    
def print_fruits(fruits):
    for fruit in fruits:
        print('~', fruit)
        
        
def main():
    fruits = get_fruits()
    print_fruits(fruits)
    
    
if __name__ == '__main__':
    main()
    
