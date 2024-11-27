from byubit import Bit


def still_fields_remaining(bit):
    return bit.front_clear()


def enter_field(bit):
    bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def paint_column(bit):
    bit.paint("green")
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint("green")


def next_column(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.move()


def paint_field(bit):
    while bit.front_clear():
        paint_column(bit)
        next_column(bit)
    paint_column(bit)
    bit.snapshot("finished paint")


def leave_field(bit):
    bit.right()
    bit.right()
    while not bit.left_clear():
        bit.move()
    bit.left()
    bit.move()


@Bit.worlds('soccer', 'soccer2')
def go(bit):
    while still_fields_remaining(bit):
        enter_field(bit)
        paint_field(bit)
        leave_field(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
