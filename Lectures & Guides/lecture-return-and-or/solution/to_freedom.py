from byubit import Bit


@Bit.run('freedom')
def go(bit):
    while not (bit.left_clear() and bit.right_clear()):
        bit.move()

