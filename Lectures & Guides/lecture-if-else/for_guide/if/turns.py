from byubit import Bit


def respond_to_square(bit):
    if bit.is_red():
        bit.left()
    elif bit.is_green():
        bit.right()
    else:
        bit.paint('blue')


@Bit.worlds('turns')
@Bit.pictures()
def go(bit):
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        respond_to_square(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
