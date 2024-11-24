from byubit import Bit


@Bit.worlds('green-path')
def walk(bit):
    while bit.is_green():
        bit.move()


if __name__ == '__main__':
    walk(Bit.new_bit)
