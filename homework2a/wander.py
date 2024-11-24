from byubit import Bit


def change_direction(bit):
    if bit.is_green():
        bit.left()
    elif bit.is_blue():
        bit.right()


def leave_trail(bit):
    if bit.is_empty():
        bit.paint("red")


@Bit.worlds('wander', 'wander2')
def go(bit):
    while bit.front_clear():
        leave_trail(bit)
        bit.move()
        change_direction(bit)
    leave_trail(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
