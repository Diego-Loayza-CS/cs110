from byubit import Bit


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


@Bit.empty_world(17, 8)
def fireworks(bit):
    one_firework(bit)
    bit.move()
    bit.move()
    one_firework(bit)
    bit.move()
    bit.move()
    one_firework(bit)


if __name__ == '__main__':
    fireworks(Bit.new_bit)
