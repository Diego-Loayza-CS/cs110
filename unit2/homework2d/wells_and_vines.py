from byubit import Bit


def back_to_line(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()


def paint_and_return(bit, color):
    while bit.front_clear():
        bit.move()
        bit.paint(color)
    back_to_line(bit)


def paint_vine(bit):
    color = bit.get_color()

    if bit.right_clear():
        bit.right()
        paint_and_return(bit, color)
        bit.right()

    elif bit.left_clear():
        bit.left()
        paint_and_return(bit, color)
        bit.left()


@Bit.worlds('wells-and-vines', 'wells-and-vines2')
def run(bit):
    while bit.front_clear():
        if not bit.is_empty():
            paint_vine(bit)
        bit.move()
    paint_vine(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
