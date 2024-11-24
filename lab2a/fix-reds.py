from byubit import Bit


def move_until_green(bit):
    while not bit.is_green():
        bit.move()


def paint_until_end(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_red():
            bit.paint("blue")


@Bit.worlds('fix-reds')
def run(bit):
    move_until_green(bit)
    paint_until_end(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
