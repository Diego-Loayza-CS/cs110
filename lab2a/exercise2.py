from byubit import Bit


def follow_rules(bit):
    if bit.is_on_blue():
        bit.turn_left()
    elif bit.is_on_green():
        bit.turn_right()
    elif bit.is_on_red():
        bit.turn_right()
        bit.turn_right()


@Bit.worlds('exercise2')
def go(bit):
    while bit.can_move_front():
        bit.move()
        follow_rules(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
