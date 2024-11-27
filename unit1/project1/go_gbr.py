from byubit import Bit


def greens(bit):
    while not bit.is_green():
        bit.paint("green")
        bit.move()
    bit.right()


def blues(bit):
    while not bit.is_blue():
        bit.paint("blue")
        bit.move()
    bit.left()


def reds(bit):
    while not bit.is_red():
        bit.paint("red")
        bit.move()


@Bit.worlds("go-go-go", "og-og-og")
def go_gbr(bit):
    greens(bit)
    bit.move()
    blues(bit)
    bit.move()
    reds(bit)


if __name__ == '__main__':
    go_gbr(Bit.new_bit)
