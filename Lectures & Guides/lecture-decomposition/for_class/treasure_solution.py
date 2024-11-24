# Solution
from byubit import Bit


def in_cave(bit):
    return not bit.left_clear() and not bit.right_clear()


def follow_turn_instructions(bit):
    if bit.is_red():
        bit.left()
        bit.snapshot('Turned left')
    elif bit.is_blue():
        bit.right()
        bit.snapshot('Turned right')
        

def get_to_cave(bit):
    """
    Bit ends just inside the cave (black on left and right)
    To get there, Bit must turn right on blue and left on red.
    """
    while not in_cave(bit):
        bit.move()
        follow_turn_instructions(bit)
        bit.paint('green')

        
def turn_to_clear(bit):
    """If left is clear, turn left, otherwise turn right."""
    if bit.left_clear():
        bit.left()
        bit.snapshot('Turned left')
        
    else:
        bit.right()
        bit.snapshot('Turned right')
        
        
def find_treasure(bit):
    """Bit ends at the treasure (red square). If the front is blocked, turn in the direction that is clear."""
    while not bit.is_red():
        if not bit.front_clear():
            turn_to_clear(bit)
        bit.paint('green')
        bit.move()
        

@Bit.worlds('treasure')
def go(bit):
    bit.paint('green')
    
    get_to_cave(bit)
    bit.snapshot('Found cave')

    find_treasure(bit)
    
    bit.paint('green')
    
if __name__ == '__main__':
    go(Bit.new_bit)
