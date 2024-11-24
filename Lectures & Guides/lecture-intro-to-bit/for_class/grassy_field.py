from byubit import Bit


@Bit.worlds("grassy_field")
def make_sky(bit):
    bit.paint('blue')
    bit.move()

    bit.paint('blue')
    bit.move()

    bit.paint('blue')
    bit.move()

    bit.paint('blue')
    bit.move()

    bit.paint('blue')
    bit.move()

    bit.paint('blue')


if __name__ == '__main__':
    make_sky(Bit.new_bit)
