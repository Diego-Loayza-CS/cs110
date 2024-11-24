from byubit import Bit


def handle_turns(bit):
    if bit.is_red():
        bit.left()
        
    elif bit.is_green():
        bit.right()
        
    else:
        bit.paint('blue')

        
@Bit.worlds('turns')
def go(bit):
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        handle_turns(bit)
            
            
if __name__ == '__main__':
    go(Bit.new_bit)
