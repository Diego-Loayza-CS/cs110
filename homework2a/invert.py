from byubit import Bit


def change_square(bit):
    if bit.is_on_white():
        bit.paint("blue")
    elif bit.is_blue():
        bit.paint("white")


@Bit.worlds('invert', 'invert2', 'invert-careful')
def go(bit):
    while bit.front_clear():
        change_square(bit)
        bit.move()
    change_square(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
