from byubit import Bit


@Bit.empty_world(5, 8)
def one_firework(bit):
    bit.move()
    bit.move()
    bit.left()
    bit.move()
    bit.move()
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("red")
    bit.left()
    bit.move()
    bit.right()
    bit.move()
    bit.paint("green")
    bit.right()
    bit.move()
    bit.move()
    bit.paint("green")
    bit.move()
    bit.right()
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.left()


if __name__ == '__main__':
    one_firework(Bit.new_bit)
