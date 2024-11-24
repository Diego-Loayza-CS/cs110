from byubit import Bit


def should_keep_going(bit):
    return bit.front_clear() and bit.is_blue()


@Bit.worlds('blue-trail', 'blue-trail2')
def go(bit):
    while should_keep_going(bit):
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
