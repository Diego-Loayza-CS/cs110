from byubit import Bit


@Bit.empty_world(5, 3)
def go_go_go(bit):
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.paint('green')


if __name__ == '__main__':
    go_go_go(Bit.new_bit)