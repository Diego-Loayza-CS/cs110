from byubit import Bit


def turn_or_change(bit):
    if bit.is_on_red():
        bit.turn_left()

    elif bit.is_on_green():
        bit.paint('blue')

    elif bit.is_on_blue():
        bit.paint('green')


@Bit.worlds('exercise1')
def go(bit):
    while bit.can_move_front():
        bit.move()
        turn_or_change(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
