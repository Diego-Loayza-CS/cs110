from byubit import Bit


def change_square(bit):
    if bit.right_clear():
        bit.paint("red")

    elif bit.left_clear():
        bit.paint("green")

    else:
        bit.paint("blue")


@Bit.worlds('holes')
def run(bit):
    bit.paint("blue")
    while bit.front_clear():
        bit.move()
        change_square(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
