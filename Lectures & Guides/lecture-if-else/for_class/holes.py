from byubit import Bit


def fix(bit):
    if bit.right_clear():
        bit.paint("red")

    elif bit.left_clear():
        bit.paint("green")

    else:
        bit.paint("blue")


@Bit.worlds('holes')
def run(bit):
    fix(bit)
    while bit.front_clear():
        bit.move()
        fix(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
