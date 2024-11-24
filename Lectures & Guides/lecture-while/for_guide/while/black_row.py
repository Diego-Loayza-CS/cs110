from byubit import Bit


@Bit.worlds('black-row')
def go(bit):
    while bit.right_clear():
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
