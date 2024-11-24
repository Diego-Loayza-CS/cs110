# Solution
from byubit import Bit, use_text_renderer
use_text_renderer()

def go_up(bit):
    bit.right()
    while bit.left_clear():
        bit.move()
        bit.paint('green')
    bit.move()
    bit.left()
    
    
@Bit.worlds('for_class/worlds/elevators')
@Bit.pictures('images/', ext='svg', title='Elevators')
def run(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_green():
            go_up(bit)
            
            
if __name__ == '__main__':
    run(Bit.new_bit)
