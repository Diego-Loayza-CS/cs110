from byubit import Bit


def decide_escalate(bit):
    if bit.left_clear():
        bit.left()

        while bit.right_clear():
            bit.move()
            bit.paint("green")
        bit.move()
        bit.right()

    else:
        bit.right()

        while bit.left_clear():
            bit.move()
            bit.paint("green")
        bit.move()
        bit.left()


@Bit.worlds('elevators', 'more-elevators')
def run(bit):
    while bit.front_clear():
        if not bit.is_green():
            bit.move()
        else:
            decide_escalate(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
