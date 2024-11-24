# Solution
from byubit import Bit


def jump(bit):
    """
    Jump up the ledge.
    Start facing the wall at the bottom of the ledge.
    End at the top, facing right, with an empty square underneath (i.e. not "on" the ledge yet)
    
           > 
      *     *
     >*     *
    ***   ***
    """
    bit.left()
    while not bit.right_clear():
        bit.move()
    bit.right()
    
    
def plant_tree(bit):
    """If the square below is black, plant a tree."""
    if not bit.right_clear():
        bit.paint('green')
        

def go_up(bit):
    """
    Get Bit to the top of the mountain.
    
    Bit ends at the top of the mountain facing right with an empty square to his right.
    Bit paints green all the squares immediately above a black square.
    """
    while not bit.right_clear():
        if not bit.front_clear():
            jump(bit)
        bit.move()
        plant_tree(bit)
        
        
def drop(bit):
    """Bit starts facing right with empty beneath, and ends facing right with black beneath."""
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    
    
def go_down(bit):
    """
    Bit starts at the top of the mountain (facing right, empty space beneath) and descends to the right,
      ending in the corner.
    """
    while bit.front_clear():
        if bit.right_clear():
            drop(bit)
        plant_tree(bit)
        bit.move()


@Bit.worlds('y-mountain', 'mountain')
@Bit.pictures()
def run(bit):
    bit.paint('green')
    
    # Go up
    go_up(bit)
    bit.snapshot('Top')
                        
    # Go down
    go_down(bit)
    
    bit.paint('green')


if __name__ == '__main__':
    run(Bit.new_bit)
