from byubit import Bit


def look_for_stem(bit):
    while not bit.is_green():
        bit.move()


def grow_flower(bit):
    bit.left()
    bit.move()
    bit.paint("red")
    bit.right()
    bit.right()
    bit.move()
    bit.left()


@Bit.worlds('flowers')
def go(bit):
    while bit.front_clear():
        look_for_stem(bit)
        grow_flower(bit)
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
