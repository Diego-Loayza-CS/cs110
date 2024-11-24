# Solution
from byubit import Bit


def maybe_turn(bit):
    if bit.is_blue():
        bit.left()
    elif bit.is_green():
        bit.right()


@Bit.worlds('fly')
def run(bit):
    while not bit.is_red():
        bit.move()
        maybe_turn(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
