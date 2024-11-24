# Solution
from byubit import Bit



def go(bit):
    while bit.front_clear():
        bit.move()

        
def go_blue(bit):
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        bit.paint('blue')
        
        
def turn_around(bit):
    bit.left()
    bit.left()
    
    
def fill_column_with_blue(bit):
    """
    Bit starts facing up
    Bit turns right and fills the row with blue
    Bit returns to the left and turns to face up
    """
    bit.left()
    go_blue(bit)
    turn_around(bit)
    go(bit)
    bit.left()
    

@Bit.empty_world(6, 6, name='Blue Ocean')
def run(bit):

    fill_column_with_blue(bit)
    while bit.front_clear():
        bit.move()
        fill_column_with_blue(bit)
        
    turn_around(bit)
    go(bit)
    turn_around(bit)
    

if __name__ == '__main__':
    run(Bit.new_bit)
