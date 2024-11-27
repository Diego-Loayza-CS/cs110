from byubit import Bit


def has_neighbour(bit):
    return not bit.right_clear() or not bit.left_clear()


@Bit.worlds('clear-green', 'clear-green2')
def run(bit):
    while bit.front_clear():
        if has_neighbour(bit):
            bit.erase()
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
