from byubit import Bit


@Bit.empty_world(5, 3)
def main(bit):
    bit.move()
    bit.move()
    bit.paint("green")


if __name__ == '__main__':
    main(Bit.new_bit)