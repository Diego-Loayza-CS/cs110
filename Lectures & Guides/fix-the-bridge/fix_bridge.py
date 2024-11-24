from byubit import Bit


def to_bridge(bit):
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()
    bit.left()


def bridge_construct(bit):
    bit.move()
    while bit.front_clear():
        bit.paint("red")
        bit.move()
    bit.left()
    bit.move()
    bit.right()


def to_end(bit):
    while bit.front_clear():
       bit.move()


@Bit.worlds('fix-bridge', 'fix-another-bridge')
def go_fix_the_bridge(bit):
    to_bridge(bit)
    bridge_construct(bit)
    to_end(bit)


if __name__ == '__main__':
    go_fix_the_bridge(Bit.new_bit)
