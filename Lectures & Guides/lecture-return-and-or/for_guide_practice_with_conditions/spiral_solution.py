# Solution 
from byubit import Bit


def end_of_spiral(bit):
    return not bit.front_clear() and not bit.left_clear()


@Bit.worlds('spiral')
def run(bit):
    bit.paint('blue')
    while not end_of_spiral(bit): 
        if not bit.front_clear():
            bit.left()
            bit.snapshot('Turned left')
        bit.move()
        bit.paint('blue')


if __name__ == '__main__':
    run(Bit.new_bit)
