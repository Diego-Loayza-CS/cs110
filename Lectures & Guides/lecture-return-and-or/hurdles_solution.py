# solution
from byubit import Bit, use_text_renderer
use_text_renderer()


def is_finished(bit):
    return not bit.front_clear() and not bit.left_clear()


def go_green(bit):
    """
    Bit moves forward until blocked, painting green on the way
    The first square is not painted; the last square IS painted.
    """
    while bit.front_clear():
        bit.move()
        bit.paint('green')

        
def cover_green(bit):
    """
    Bit moves forward until the right side is clear, painting green on the way
    The first square is not painted; the last square IS painted.
    """
    while not bit.right_clear():
        bit.move()
        bit.paint('green')
              

def jump_hurdle(bit):
    """
    Bit starts at base of hurdle on left side facing right
    Bit ends at base of hurdle on right side facing right
    """
    # Up
    bit.left()
    cover_green(bit)
    bit.right()
    
    # Over
    bit.move()
    bit.paint('green')
    cover_green(bit)
    
    # Down
    bit.right()
    go_green(bit)
    bit.left()
    
    bit.snapshot('Hurdle cleared!')

    
@Bit.worlds('for_class/worlds/hurdles', 'for_class/worlds/more-hurdles')
@Bit.pictures('images/', ext='svg', title='Hurdles')
def run(bit):
    bit.paint('green')
    while not is_finished(bit):
        if not bit.front_clear():
            jump_hurdle(bit)
        else:
            bit.move()
            bit.paint('green')
            # go_green(bit)
            
            
if __name__ == '__main__':
    run(Bit.new_bit)
    
