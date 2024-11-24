from byubit import Bit


def is_frog(bit):
    """Square is a frog if it is green and above a black square"""
    return bit.is_green() and not bit.right_clear()


@Bit.worlds('frog-on-rock')
@Bit.pictures()
def go(bit):
    while bit.front_clear():
        bit.move()
        if is_frog(bit):
            bit.erase()


if __name__ == '__main__':
    go(Bit.new_bit)
