from byubit import Bit


def to_green(bit):
    bit.left()
    while not bit.is_green():
        bit.paint("red")
        bit.move()
    bit.paint("red")


def descend(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds("banner", "another_banner")
def banner(bit):
    while bit.front_clear():
        to_green(bit)
        descend(bit)
        bit.move()
    to_green(bit)
    descend(bit)


if __name__ == '__main__':
    banner(Bit.new_bit)
