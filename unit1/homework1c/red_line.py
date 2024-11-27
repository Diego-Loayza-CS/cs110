from byubit import Bit


def to_red(bit):
    while not bit.is_red():
        bit.move()
    bit.right()


def red_line(bit):
    while not bit.is_red():
        bit.paint("red")
        bit.move()
    bit.right()


def to_room(bit):
    while bit.left_clear():
        bit.move()


@Bit.worlds('red-line')
def draw_line(bit):
    to_red(bit)
    bit.move()
    red_line(bit)
    to_room(bit)


if __name__ == "__main__":
    draw_line(Bit.new_bit)
