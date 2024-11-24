from byubit import Bit


def change_squares(bit):
    if bit.is_red():
        bit.paint('blue')
    else:
        bit.paint('green')


@Bit.worlds('more-red-dots')
def go(bit):
    while bit.front_clear():
        bit.move()
        change_squares(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
