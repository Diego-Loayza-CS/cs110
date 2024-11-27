from byubit import Bit


def move_while_clear(bit):
    """ Moves while front is clear. Paints green as it goes. """
    while bit.front_clear():
        bit.paint("green")
        bit.move()


def move_while_not_red(bit):
    """ Moves while current square is not red. Paints green as it goes. Does not paint the red square green. """
    while not bit.is_red():
        bit.paint("green")
        bit.move()


@Bit.worlds('maze')
def solve_maze(bit):
    move_while_clear(bit)
    bit.left()
    move_while_clear(bit)
    bit.right()
    move_while_clear(bit)
    bit.right()
    move_while_not_red(bit)


if __name__ == "__main__":
    solve_maze(Bit.new_bit)
