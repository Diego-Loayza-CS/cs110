from byubit import Bit


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

def get_the_colors(bit):
    first = bit.get_color()
    bit.erase()
    bit.move()
    second = bit.get_color()
    bit.erase()
    bit.move()
    third = bit.get_color()
    bit.erase()
    return first, second, third


def paint_ttt(bit, color1, color2, color3):
    paint_t(bit, color1)
    paint_t(bit, color2)
    paint_t(bit, color3)


@Bit.worlds('color_tt', 'color_tt2')
def run(bit):
    color1, color2, color3 = get_the_colors(bit)
    go_to_start(bit)
    paint_ttt(bit, color1, color2, color3)


if __name__ == '__main__':
    run(Bit.new_bit)
