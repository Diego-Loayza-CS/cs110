from byubit import Bit


def green_start(bit):
    while not bit.is_green():
        bit.move()


def remove_rocks(bit):
    while not bit.is_green():
        if bit.is_blue():
            bit.erase()
        bit.move()


def to_end(bit):
    while bit.front_clear():
        bit.move()


@Bit.worlds('remove-rocks', 'remove-rocks2')
def run(bit):
    green_start(bit)
    bit.move()
    remove_rocks(bit)
    to_end(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
