from byubit import Bit


def spiral_incomplete(bit):
    return not bit.is_green()


@Bit.worlds('paint-the-box', 'paint-another-box')
def run(bit):
    while spiral_incomplete(bit):
        if bit.front_clear():
            bit.paint("green")
            bit.move()
        else:
            bit.left()
            bit.paint("green")
            bit.move()
    bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)
