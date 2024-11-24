# Solution 
from byubit import Bit, use_text_renderer
use_text_renderer()

def process_square(bit):
    if bit.right_clear():
        bit.paint('red')
        
    elif bit.left_clear():
        bit.paint('green')
        
    else:
        bit.paint('blue')

        
@Bit.worlds('for_class/worlds/holes')
@Bit.pictures('images/', title='Holes', ext='svg')
def run(bit):
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        process_square(bit)
            
            
if __name__ == '__main__':
    run(Bit.new_bit)
