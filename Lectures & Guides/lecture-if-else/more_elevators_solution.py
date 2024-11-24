# Solution
from byubit import Bit, use_text_renderer
use_text_renderer()

def go_left_up(bit):
    bit.left()
    while bit.right_clear():
        bit.move()
        bit.paint('green')
    bit.move()
    bit.right()

    
def go_right_up(bit):
    bit.right()
    while bit.left_clear():
        bit.move()
        bit.paint('green')
    bit.move()
    bit.left()

    
def go_up(bit):
    if bit.left_clear():
        go_left_up(bit)
    else:
        go_right_up(bit)
        
        
@Bit.worlds('for_class/worlds/elevators', 'for_class/worlds/more-elevators')
@Bit.pictures('images/', ext='svg', title='More Elevators')
def run(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_green():
            go_up(bit)
          
        
if __name__ == '__main__':
    run(Bit.new_bit)
