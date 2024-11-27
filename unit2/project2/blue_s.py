from byubit import Bit


def found_s(bit):
    return bit.is_green()


def go(bit):
    while bit.front_clear():
        bit.move()


def to_top(bit):
    bit.left()
    go(bit)
    bit.right()
    go(bit)


def paint_until_wall(bit):
    while bit.front_clear():
        bit.paint("blue")
        bit.move()
    bit.paint("blue")


def paint_upper_part(bit):
    bit.left()
    bit.left()
    paint_until_wall(bit)
    bit.left()
    paint_until_wall(bit)
    bit.left()


def paint_lower_part(bit):
    paint_until_wall(bit)
    bit.right()
    paint_until_wall(bit)


def leave_trail(bit):
    paint_upper_part(bit)
    bit.move()
    bit.right()
    paint_lower_part(bit)


def return_main_line(bit):
    bit.right()
    bit.right()
    go(bit)
    bit.left()
    go(bit)
    bit.right()


def paint_s(bit):
    to_top(bit)
    leave_trail(bit)
    return_main_line(bit)


@Bit.worlds('blue-s', 'big-blue-s')
def run(bit):
    while bit.front_clear():
        if found_s(bit):
            bit.snapshot("found s")
            paint_s(bit)
            bit.snapshot("painted s")
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
