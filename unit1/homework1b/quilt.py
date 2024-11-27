from byubit import Bit


def red_vertical(bit):
    bit.paint("red")
    bit.left()
    bit.move()
    bit.paint("red")
    bit.move()
    bit.paint("red")
    bit.right()


def green_horizontal(bit):
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.right()


def green_vertical(bit):
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.right()


def green_circle(bit):
    green_horizontal(bit)
    green_vertical(bit)
    green_horizontal(bit)
    bit.move()
    bit.paint("green")
    bit.right()


def center_to_red_start(bit):
    bit.paint("blue")
    bit.move()
    bit.right()
    bit.move()
    bit.left()
    bit.move()


def return_bottom(bit):
    bit.right()
    bit.move()
    bit.move()
    bit.left()


def column_plus_square(bit):
    red_vertical(bit)
    bit.move()
    green_circle(bit)
    bit.move()
    center_to_red_start(bit)
    red_vertical(bit)
    return_bottom(bit)


@Bit.worlds("quilt")
def make_a_quilt(bit):
    column_plus_square(bit)
    column_plus_square(bit)
    column_plus_square(bit)


if __name__ == '__main__':
    make_a_quilt(Bit.new_bit)
