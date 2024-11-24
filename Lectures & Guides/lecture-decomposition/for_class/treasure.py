from byubit import Bit


def enter_cave(bit):
    while bit.right_clear() or bit.left_clear():
        if bit.is_red():
            bit.left()

        elif bit.is_blue():
            bit.right()

        bit.paint("green")
        bit.move()


def to_treasure(bit):
    while not bit.is_red():
        bit.paint("green")
        if bit.front_clear():
            bit.move()
        elif bit.right_clear():
            bit.right()
        elif bit.left_clear():
            bit.left()


@Bit.worlds('treasure')
def go(bit):
    enter_cave(bit)
    to_treasure(bit)
    bit.paint("green")


if __name__ == '__main__':
    go(Bit.new_bit)
