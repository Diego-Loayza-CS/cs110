from byubit import Bit


def leap(bit):
    if bit.can_move_front():
        bit.move()
    if bit.can_move_front():
        bit.move()
    if bit.can_move_front():
        bit.move()


def paint_spots(bit):
    while bit.can_move_front():
        bit.paint('blue')
        leap(bit)
    bit.paint('blue')


def fill_green(bit):
    while bit.can_move_front():
        bit.paint('green')
        bit.move()
    bit.paint('green')


@Bit.empty_world(6, 3)
def go(bit):
    fill_green(bit)
    bit.turn_left()
    bit.turn_left()
    paint_spots(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
