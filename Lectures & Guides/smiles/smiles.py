from byubit import Bit


def move_into_place(bit):
    """ Gets into position to draw a smile by moving to the
        top left eye and then turning right.
    """
    bit.move()
    bit.turn_right()


def left_side(bit):
    """ Paints the top left eye and the  left corner of the smile.
        Ends up facing to the right on the bottom left of the smile.
    """
    bit.paint('blue')
    bit.move()
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.turn_left()


def bottom(bit):
    """ Paints the bottom part of the smile. Ends up facing right,
        in the bottom right corner of the smile.
    """
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.turn_left()


def right_side(bit):
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.move()
    bit.paint('blue')
    bit.turn_right()


def draw_smile(bit):
    move_into_place(bit)
    left_side(bit)
    bottom(bit)
    right_side(bit)


@Bit.worlds('smiles')
def run(bit):
    draw_smile(bit)
    bit.move()
    draw_smile(bit)
    bit.move()
    draw_smile(bit)
    bit.move()
    draw_smile(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
