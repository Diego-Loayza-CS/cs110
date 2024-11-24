from byubit import Bit


def go(bit, color):
    while bit.front_clear():
        bit.move()
        bit.paint(color)
        
        
def turn_around(bit):
    bit.left()
    bit.left()
    
    
def fill_column(bit):
    bit.left()
    color = bit.get_color()
    go(bit, color)
    turn_around(bit)
    go(bit, color)
    bit.left()
    bit.snapshot(color)

    
@Bit.worlds('colors')
def fill_colorful(bit):
    fill_column(bit)
    while bit.front_clear():
        bit.move()
        fill_column(bit)
        
        
if __name__ == '__main__':
    fill_colorful(Bit.new_bit)
