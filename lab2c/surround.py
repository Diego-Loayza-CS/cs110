from byubit import Bit


def surround(bit):
    while not bit.is_green():
        if not bit.right_clear():
            bit.paint("green")
            bit.move()
        else:
            bit.right()
            bit.move()


def leave_block(bit):
    while not bit.right_clear():
        bit.move()


def block_found(bit):
    return not bit.right_clear()


@Bit.worlds('surround', 'surround2')
def run(bit):
    while bit.front_clear():
        bit.move()
        if block_found(bit):
            surround(bit)
            leave_block(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
