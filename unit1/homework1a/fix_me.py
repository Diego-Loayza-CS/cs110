from byubit import Bit


@Bit.worlds('fix-me')
def fix_me(bit):
    bit.paint('green')
    bit.move()
    bit.paint('green')
    bit.move()
    bit.turn_left()
    bit.paint('green')
    bit.move()
    bit.paint('blue')


if __name__ == '__main__':
    fix_me(Bit.new_bit)
