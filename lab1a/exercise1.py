from byubit import Bit


@Bit.empty_world(5, 3)
def do_stuff(bit):
    bit.paint('blue')
    bit.move()
    bit.move()
    bit.paint('green')
    bit.turn_left()
    bit.move()
    bit.move()
    bit.paint('red')


if __name__ == '__main__':
    do_stuff(Bit.new_bit)
