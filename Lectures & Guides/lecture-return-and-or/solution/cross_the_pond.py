from byubit import Bit


@Bit.run('frog-on-rock')
def go(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_green() and not bit.right_clear():
            bit.erase()
