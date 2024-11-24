from byubit import Bit


def get_to_cave(bit):
    while bit.right_clear() or bit.left_clear():
        if bit.is_red():
            bit.left()
        elif bit.is_blue():
            bit.right()
        bit.paint("green")
        bit.move()


def navigate_cave(bit):
    while not bit.is_red():
        if bit.right_clear():
            bit.right()
        elif bit.left_clear():
            bit.left()
        bit.paint("green")
        bit.move()


def claim_treasure(bit):
    bit.paint("green")


@Bit.worlds('treasure')
def go(bit):
    get_to_cave(bit)
    navigate_cave(bit)
    claim_treasure(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
