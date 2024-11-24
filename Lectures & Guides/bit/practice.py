from byubit import Bit


@Bit.empty_world(5, 3)
def go(bit):
    bit.move()
    bit.move()
    bit.move()
    bit.left()
    bit.move()
    bit.paint("green")

if __name__ == '__main__':
    go(Bit.new_bit)
