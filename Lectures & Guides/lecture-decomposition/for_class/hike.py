from byubit import Bit


def path_ahead(bit):
    return bit.front_clear()


def escalate(bit):
    bit.paint("green")
    bit.left()
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()


def walk(bit):
    bit.paint("green")
    bit.move()


def on_floor(bit):
    return not bit.right_clear()


def jump_down(bit):
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.paint("green")
    bit.left()


@Bit.worlds('y-mountain', 'mountain')
def run(bit):
    while on_floor(bit):
        if path_ahead(bit):
            walk(bit)
        else:
            escalate(bit)
    while path_ahead(bit):
        if on_floor(bit):
            walk(bit)
        else:
            jump_down(bit)
    bit.paint("green")


if __name__ == '__main__':
    run(Bit.new_bit)
