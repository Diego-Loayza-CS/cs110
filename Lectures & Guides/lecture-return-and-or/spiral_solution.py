# Solution 
from byubit import Bit, use_text_renderer
use_text_renderer()

def end_of_spiral(bit):
    return not bit.front_clear() and not bit.left_clear()


@Bit.worlds('for_class/worlds/spiral')
@Bit.pictures('images/', ext='svg', title='Spiral')
def run(bit):
    bit.paint('blue')
    while not end_of_spiral(bit): 
        if not bit.front_clear():
            bit.left()
            bit.snapshot('Turned left')
        bit.move()
        bit.paint('blue')
        
        
if __name__ == '__main__':
    run(Bit.new_bit)
    
