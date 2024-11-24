from byubit import Bit


def bit_free(bit):
    return bit.right_clear() and bit.left_clear()


@Bit.worlds('freedom')
def go(bit):
    while not bit_free(bit):
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
