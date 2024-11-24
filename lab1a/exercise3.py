from byubit import Bit


@Bit.empty_world(3, 3)
def do_stuff(bit):
    bit.paint('blue')
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.turn_left()
    bit.paint('green')
    bit.move()
    bit.move()
    bit.paint('red')


if __name__ == '__main__':
    do_stuff(Bit.new_bit)
