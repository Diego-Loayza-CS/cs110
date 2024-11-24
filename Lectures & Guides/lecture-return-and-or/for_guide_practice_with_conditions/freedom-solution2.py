from byubit import Bit


def keep_moving(bit):
    return not bit.left_clear() or not bit.right_clear()


@Bit.worlds('freedom')
def go(bit):
    while keep_moving(bit):
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
