from byubit import Bit


@Bit.worlds('blue-dot')
def go_to_blue(bit):
    while not bit.is_blue():
        bit.move()


if __name__ == '__main__':
    go_to_blue(Bit.new_bit)
