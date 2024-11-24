from byubit import Bit


def jump_down(bit):
    bit.right()
    while bit.front_clear():
        bit.paint("green")
        bit.move()
    bit.left()


def descend_mountain(bit):
    while not bit.is_blue():
        bit.paint("green")
        if bit.right_clear():
            jump_down(bit)
        else:
            bit.move()


def swim_river(bit):
    while bit.is_blue():
        if bit.right_clear():
            bit.right()
            bit.move()

        elif not bit.front_clear():
            bit.left()

        elif bit.front_clear():
            bit.move()
        bit.snapshot("move")


def cycle(bit):
    bit.right()
    while bit.front_clear():
        bit.move()
        bit.paint("red")


@Bit.worlds('bitathon', 'bitathon2')
def run(bit):
    descend_mountain(bit)
    swim_river(bit)
    cycle(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
