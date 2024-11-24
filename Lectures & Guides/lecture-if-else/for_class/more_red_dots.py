from byubit import Bit


def process_square(bit):
    if bit.is_red():
        bit.paint('blue')
    else:
        bit.paint('green')
        
        
@Bit.worlds('more-red-dots')
def go(bit):
    while bit.front_clear():
        bit.move()
        process_square(bit)
        
        
if __name__ == '__main__':
    go(Bit.new_bit)
