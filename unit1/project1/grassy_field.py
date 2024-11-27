from byubit import Bit


def fill_horizontal(bit):
    while bit.front_clear():
        bit.paint("green")
        bit.move()
    bit.paint("green")


def return_horizontal(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.left()


def climb(bit):
    bit.left()
    bit.move()
    bit.right()


def to_finish(bit):
    while bit.front_clear():
        bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds("grassy_field", "big_grassy_field")
def run(bit):
    fill_horizontal(bit)
    return_horizontal(bit)
    while bit.left_clear():
        climb(bit)
        fill_horizontal(bit)
        return_horizontal(bit)
    to_finish(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
