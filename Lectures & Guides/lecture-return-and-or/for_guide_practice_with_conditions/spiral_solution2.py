# Solution 
from byubit import Bit


@Bit.worlds('spiral')
def run(bit):
    while bit.front_clear():
        bit.paint('blue')
        bit.move()
        if not bit.front_clear():
            bit.left()

    bit.paint('blue')


if __name__ == '__main__':
    run(Bit.new_bit)
