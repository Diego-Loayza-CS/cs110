from byubit import Bit


@Bit.worlds('missing-smile')
def make_me_smile(bit):
    # Implement me!
    pass
    bit.move()
    bit.move()
    bit.right()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.right()
    bit.move()
    bit.paint("blue")
    bit.left()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.left()
    bit.move()
    bit.paint("blue")


if __name__ == '__main__':
    make_me_smile(Bit.new_bit)
