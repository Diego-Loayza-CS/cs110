from byubit import Bit


@Bit.worlds('another-black-row')
def go(bit):
    while not bit.right_clear():
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
