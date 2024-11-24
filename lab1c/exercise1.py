from byubit import Bit


def green_line(bit):
    while bit.can_move_front():
        bit.move()
        bit.paint('green')


def blue_line(bit):
    while bit.can_move_front():
        bit.paint('blue')
        bit.move()


@Bit.empty_world(5, 3)
def go(bit):
    green_line(bit)
    bit.turn_left()
    blue_line(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
