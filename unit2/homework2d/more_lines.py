from byubit import Bit


def paint_line(bit):
    color = bit.get_color()
    bit.move()
    while bit.is_empty():
        bit.paint(color)
        bit.move()


def go_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.right()


def escalate(bit):
    bit.left()
    bit.move()
    bit.right()


def paint_row(bit):
    while bit.front_clear():
        if not bit.is_empty():
            paint_line(bit)
        bit.move()
    go_back(bit)


def go_to_start(bit):
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('more-lines', 'more-lines2')
def run(bit):
    while bit.left_clear():
        paint_row(bit)
        escalate(bit)
    paint_row(bit)
    go_to_start(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
