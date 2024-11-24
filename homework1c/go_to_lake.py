from byubit import Bit


def to_red(bit):
    while not bit.is_red():
        bit.paint("green")
        bit.move()


def to_lake(bit):
    while bit.front_clear():
        bit.paint("green")
        bit.move()


@Bit.worlds('go-to-lake', 'go-to-another-lake')
def go(bit):
    to_red(bit)
    bit.left()
    bit.move()
    to_lake(bit)


if __name__ == "__main__":
    go(Bit.new_bit)
