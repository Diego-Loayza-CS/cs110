from byubit import Bit


@Bit.worlds('blocked')
def blocked(bit):
    bit.move()


if __name__ == '__main__':
    blocked(Bit.new_bit)
