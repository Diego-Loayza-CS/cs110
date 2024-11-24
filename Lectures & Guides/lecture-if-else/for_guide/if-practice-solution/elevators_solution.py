# Solution
from byubit import Bit


def go_up(bit):
    bit.right()
    while bit.left_clear():
        bit.move()
        bit.paint('green')
    bit.move()
    bit.left()
    
    
@Bit.worlds('elevators')
@Bit.pictures()
def run(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_green():
            go_up(bit)
            
            
if __name__ == '__main__':
    run(Bit.new_bit)
