from byubit import Bit


def decide_color(bit):
    if bit.is_empty():
        bit.paint("green")
    elif bit.is_green():
        bit.paint("blue")


def decide_movement(bit):
    if bit.front_clear():
        bit.move()
    elif bit.left_clear():
        bit.left()
        bit.move()
    else:
        bit.right()
        bit.move()


@Bit.worlds('scurry', 'scurry2')
def go(bit):
    while bit.front_clear() or bit.left_clear() or bit.right_clear():
        decide_color(bit)
        decide_movement(bit)
    decide_color(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
