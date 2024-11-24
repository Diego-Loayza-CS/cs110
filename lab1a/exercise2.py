from byubit import Bit


@Bit.empty_world(3, 3)
def do_stuff(bit):
    bit.move()
    bit.paint('blue')
    bit.turn_left()
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.turn_left()
    bit.move()
    bit.paint('blue')
    bit.turn_right()
    bit.turn_right()
    bit.move()
    bit.move()
    bit.paint('blue')


if __name__ == '__main__':
    do_stuff(Bit.new_bit)
