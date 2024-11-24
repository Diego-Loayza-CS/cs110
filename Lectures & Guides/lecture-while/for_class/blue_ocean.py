from byubit import Bit


def paint_row(bit):
    while bit.can_move_front():
        bit.paint("blue")
        bit.move()
    bit.paint("blue")


def return_row(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.right()


@Bit.empty_world(6, 6)
def run(bit):
    paint_row(bit)
    return_row(bit)
    while bit.left_clear():
        bit.left()
        bit.move()
        bit.right()
        paint_row(bit)
        return_row(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
