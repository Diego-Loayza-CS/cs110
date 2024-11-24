from byubit import Bit


@Bit.worlds('red-spot')
def go(bit):
    while not bit.is_on_red():
        bit.move()

    bit.turn_left()
    bit.move()
    bit.turn_left()

    while bit.can_move_front():
        bit.move()
        bit.paint('blue')


if __name__ == '__main__':
    go(Bit.new_bit)
