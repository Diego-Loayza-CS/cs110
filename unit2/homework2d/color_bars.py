from byubit import Bit


def go_back(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def paint_column(bit, color):
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint(color)
    go_back(bit)


@Bit.worlds('color-bars', 'color-bars2')
def run(bit):
    while bit.front_clear():
        if not bit.is_empty():
            color = bit.get_color()
            paint_column(bit, color)
        bit.move()
    color = bit.get_color()
    paint_column(bit, color)


if __name__ == '__main__':
    run(Bit.new_bit)
