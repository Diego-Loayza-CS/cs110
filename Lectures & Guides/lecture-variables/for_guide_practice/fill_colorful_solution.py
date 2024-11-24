from byubit import Bit


def fill_column(bit, color):
    """
    Fills a column with a given color. Bit starts facing right and ends
    facing up at the top of the column
    """
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint(color)


def go_back(bit):
    """
    Go back to the bottom and turn to the right.
    Bit starts by facing up at the top of the column.
    Bit ends by facing right at the bottom of the column.
    """
    # turn around
    bit.right()
    bit.right()
    # go back
    while bit.front_clear():
        bit.move()
    # turn
    bit.left()


@Bit.worlds('colors')
def fill_colorful(bit):
    while bit.front_clear():
        color = bit.get_color()
        fill_column(bit, color)
        go_back(bit)
        bit.move()

    # do the last column
    color = bit.get_color()
    fill_column(bit, color)
    go_back(bit)
        
        
if __name__ == '__main__':
    fill_colorful(Bit.new_bit)
