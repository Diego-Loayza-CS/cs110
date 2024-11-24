from byubit import Bit


def diagonal_paint(bit):
    bit.paint("blue")
    bit.move()
    bit.right()
    bit.move()


def vertical_paint(bit):
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.paint("blue")


def climb_right(bit):
    bit.left()
    bit.move()
    bit.left()
    bit.move()
    bit.move()
    bit.move()


def single_y(bit):
    diagonal_paint(bit)
    bit.left()
    diagonal_paint(bit)
    vertical_paint(bit)
    climb_right(bit)
    diagonal_paint(bit)
    bit.paint("blue")
    bit.move()
    bit.move()


@Bit.worlds('y')
def paint_the_ys(bit):
    single_y(bit)
    bit.move()
    single_y(bit)


if __name__ == '__main__':
    paint_the_ys(Bit.new_bit)
