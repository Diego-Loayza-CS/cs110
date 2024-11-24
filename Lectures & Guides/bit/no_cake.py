from byubit import Bit


@Bit.empty_world(5,3)
def make_a_cake(bit):
    bit.move()
    bit.paint('red')
    bit.move()
    bit.paint('green')

if __name__ == '__main__':
    make_a_cake(Bit.new_bit)
