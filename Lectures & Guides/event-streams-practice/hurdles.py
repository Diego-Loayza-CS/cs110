from byubit import Bit


def advance(bit):
    while bit.front_clear():
        bit.paint("green")
        bit.move()


def first_turn_right(bit):
    while not bit.right_clear():
        bit.paint("green")
        bit.move()
    bit.paint("green")


def climb_mountain(bit):
    bit.left()
    first_turn_right(bit)
    bit.right()
    bit.move()
    first_turn_right(bit)
    bit.right()
    advance(bit)
    bit.left()


@Bit.worlds('hurdles', 'hurdles2')
def run(bit):
    while bit.left_clear():
        if bit.front_clear():
            advance(bit)
        else:
            climb_mountain(bit)
    bit.paint("green")


if __name__ == '__main__':
    run(Bit.new_bit)
