from byubit import Bit


def paint_eye_and_corner(bit):
    "Paint blue, skip, and blue again. End on the second blue square."
    bit.paint('blue')
    bit.move()
    bit.move()
    bit.paint('blue')
    
    
def turn_left(bit):
    bit.move()
    bit.left()
    bit.move()
    
    
def paint_bottom(bit):
    "Paint 3 blue squares in a row. End on the last blue square."
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('blue')

    
def draw_smile(bit):
    """
    Draw a smile in a 4x4 box.
    Starts on the left eye, ends on the right eye facing the original direction
    """
    bit.right()
    paint_eye_and_corner(bit)
    turn_left(bit)
    paint_bottom(bit)
    turn_left(bit)
    paint_eye_and_corner(bit)
    bit.right()
    bit.snapshot('Smile!')
    
    
@Bit.worlds('smiles')
def run(bit):
    bit.move()
    draw_smile(bit)
    
    bit.move()
    bit.move()
    
    draw_smile(bit)
    
    bit.move()
    bit.move()
    
    draw_smile(bit)
    
    bit.move()
    bit.move()
    
    draw_smile(bit)
    
    
if __name__ == '__main__':
    run(Bit.new_bit)
