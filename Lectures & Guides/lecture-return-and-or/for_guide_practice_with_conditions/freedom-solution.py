from byubit import Bit


def found_freedom(bit):
    return bit.left_clear() and bit.right_clear()


@Bit.worlds('freedom')
def go(bit):
    while not found_freedom(bit):
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
