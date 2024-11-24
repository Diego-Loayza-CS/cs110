from byubit import Bit


def change_square(bit):
    if bit.is_red():
        bit.paint('blue')


@Bit.worlds('red-dots', 'another-red-dots', 'yet-another-red-dots')
def go(bit):
    while bit.front_clear():
        bit.move()
        change_square(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
