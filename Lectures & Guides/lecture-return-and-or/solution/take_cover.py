from byubit import Bit


@Bit.run('take-cover', 'take-cover2')
def go(bit):
    while bit.left_clear() and bit.right_clear() and bit.front_clear():
        bit.move()
