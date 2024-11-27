from byubit import Bit


@Bit.worlds('red-dot')
def red_dot(bit):
    # Implement me!
    bit.move()
    bit.left()
    bit.move()
    bit.paint("red")


if __name__ == '__main__':
    red_dot(Bit.new_bit)
