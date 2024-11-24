# Solution 
from byubit import Bit


@Bit.run('spiral')
def run(bit):
    # implement
    bit.paint('blue')
    # stop when the front and the left are both not clear
    while bit.front_clear() or bit.left_clear():
        bit.move()
        bit.paint('blue')
        # turn left if the front is not clear but the left is clear
        if not bit.front_clear() and bit.left_clear():
            bit.left()
