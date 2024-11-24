from byubit import Bit


def should_be_blue(bit):
    return bit.is_red() or bit.is_green()


@Bit.worlds('red-or-green')
@Bit.pictures()
def go(bit):
    while bit.front_clear():
        bit.move()
        if should_be_blue(bit):
            bit.paint('blue')


if __name__ == '__main__':
    go(Bit.new_bit)
