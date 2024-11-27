from byubit import Bit


def go_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.right()


def invert_bit(bit):
    if bit.is_empty():
        bit.paint("blue")
    elif bit.is_blue():
        bit.erase()


def invert_row(bit):
    invert_bit(bit)
    while bit.front_clear():
        bit.move()
        invert_bit(bit)
    go_back(bit)


def escalate(bit):
    bit.left()
    bit.move()
    bit.right()


def go_to_end(bit):
    while bit.front_clear():
        bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('invert', 'invert2')
def run(bit):
    while bit.left_clear():
        invert_row(bit)
        escalate(bit)
    invert_row(bit)
    go_to_end(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
