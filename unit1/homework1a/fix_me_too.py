from byubit import Bit


@Bit.worlds('fix-me-too')
def do_more_fixing(bit):
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint("red")
    bit.move()
    bit.turn_left()
    bit.move()
    bit.paint("green")
    bit.left()
    bit.move()
    bit.move()
    bit.move()
    bit.paint('red')


if __name__ == '__main__':
    do_more_fixing(Bit.new_bit)
