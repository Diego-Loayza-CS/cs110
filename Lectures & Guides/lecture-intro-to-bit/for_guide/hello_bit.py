from byubit import Bit


@Bit.empty_world(5, 3)
@Bit.pictures()
def go(bit):
    bit.move()
    bit.move()
    bit.paint("red")

    bit.left()
    bit.move()
    bit.paint("green")

    bit.right()
    bit.move()
    bit.paint("blue")


if __name__ == '__main__':
    go(Bit.new_bit)
