from byubit import Bit


@Bit.empty_world(3, 3)
def run(bit):
    while bit.front_clear():
        bit.move()
        bit.paint('blue')
        bit.move()
        bit.paint('blue')
        bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)
