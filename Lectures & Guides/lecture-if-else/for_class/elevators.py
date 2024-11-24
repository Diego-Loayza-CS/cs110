from byubit import Bit


def escalate(bit):
    if bit.right_clear():
        bit.right()
        while bit.left_clear():
            bit.move()
            bit.paint("green")
        bit.move()
        bit.left()

    else:
        bit.left()
        while bit.right_clear():
            bit.move()
            bit.paint("green")
        bit.move()
        bit.right()


@Bit.worlds('elevators', 'more-elevators')
def run(bit):
    while bit.front_clear():
        if bit.is_green():
            escalate(bit)

        else:
            bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
