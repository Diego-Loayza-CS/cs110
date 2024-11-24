from byubit import Bit


@Bit.empty_world(5, 3)
def move_around(bit):
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
    move_around(Bit.new_bit)
