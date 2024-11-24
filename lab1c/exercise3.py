from byubit import Bit


@Bit.empty_world(5, 3)
def go(bit):
    bit.paint("red")
    bit.move()
    bit.paint("green")
    while bit.front_clear():
        bit.move()
        bit.paint("blue")


if __name__ == '__main__':
    go(Bit.new_bit)
