from byubit import Bit


def look_for_color(bit):
    while bit.is_empty():
        bit.move()


def leave_trail(bit, color):
    bit.move()
    while bit.is_empty():
        bit.paint(color)
        bit.move()


def return_row(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.right()


def paint_row(bit):
    look_for_color(bit)
    bit.snapshot("found color")
    color = bit.get_color()
    leave_trail(bit, color)
    bit.snapshot("finished trail")
    return_row(bit)
    bit.snapshot("returned to start of row")


def next_row(bit):
    bit.left()
    bit.move()
    bit.right()


def return_to_start(bit):
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('lines')
def run(bit):
    while bit.left_clear():
        paint_row(bit)
        next_row(bit)
    paint_row(bit)
    return_to_start(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
