from byubit import Bit


def leave_trail(bit, color):
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint(color)


def go_back(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def paint_column(bit):
    color = bit.get_color()
    leave_trail(bit, color)
    go_back(bit)


@Bit.worlds('colors')
def fill_colorful(bit):
    paint_column(bit)
    while bit.front_clear():
        bit.move()
        paint_column(bit)


if __name__ == '__main__':
    fill_colorful(Bit.new_bit)
