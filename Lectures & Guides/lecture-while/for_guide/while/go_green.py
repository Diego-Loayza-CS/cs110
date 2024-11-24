from byubit import Bit


@Bit.empty_world(5, 3)
def go_green(bit):
    while bit.front_clear():
        bit.paint('green')
        bit.move()


if __name__ == '__main__':
    go_green(Bit.new_bit)