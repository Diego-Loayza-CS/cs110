from byubit import Bit


def horizontal(bit):
    while not bit.right_clear():
        bit.move()
    bit.right()


def vertical(bit):
    while not bit.is_red():
        bit.move()
    bit.paint("blue")


@Bit.worlds('dive-for-treasure', 'dive-for-deep-treasure')
def dive(bit):
    horizontal(bit)
    vertical(bit)


if __name__ == "__main__":
    dive(Bit.new_bit)
