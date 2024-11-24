from byubit import Bit


@Bit.empty_world(100, 3)
@Bit.pictures()
def go_green(bit):
    bit.paint('green')
    bit.move()
    bit.paint('green')
    bit.move()
    bit.paint('green')
    bit.move()
    bit.paint('green')
    bit.move()
    bit.paint('green')


if __name__ == '__main__':
    go_green(Bit.new_bit)
