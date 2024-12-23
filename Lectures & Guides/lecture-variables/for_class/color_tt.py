from byubit import Bit


def get_next_color(bit):
    color = bit.get_color()
    bit.erase()
    bit.move()
    return color


def go(bit):
    """Go until blocked in front."""
    while bit.front_clear():
        bit.move()


def go_to_start(bit):
    """Bit starts anywhere on the board and ends in the bottom left corner facing right."""
    bit.left()
    bit.left()
    go(bit)
    bit.left()
    go(bit)
    bit.left()


def paint_t(bit, color):
    """Paint a T. Start in the bottom left of the 3x3 box. End just outside the bottom right of the 3x3 box."""
    bit.move()
    bit.left()
    bit.paint(color)
    bit.move()
    bit.paint(color)
    bit.move()
    bit.left()
    bit.move()
    bit.left()
    bit.left()
    bit.paint(color)
    bit.move()
    bit.paint(color)
    bit.move()
    bit.paint(color)
    bit.right()
    bit.move()
    bit.move()
    bit.left()
    bit.move()
    bit.snapshot('T painted')


def next_bit(bit):
    bit.erase()
    bit.move()


@Bit.worlds('color_tt', 'color_tt2')
def run(bit):
    first_color = bit.get_color()
    next_bit(bit)

    second_color = bit.get_color()
    next_bit(bit)

    third_color = bit.get_color()
    next_bit(bit)

    go_to_start(bit)

    paint_t(bit, first_color)
    paint_t(bit, second_color)
    paint_t(bit, third_color)


if __name__ == '__main__':
    run(Bit.new_bit)
