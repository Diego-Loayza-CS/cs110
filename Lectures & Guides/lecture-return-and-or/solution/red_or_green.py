from byubit import Bit


@Bit.run('red-or-green')
def go(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_red() or bit.is_green():
            bit.paint('blue')
