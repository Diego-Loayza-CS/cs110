from byubit import Bit


@Bit.empty_world(5, 3)
def make_green_square(bit):
    pass


if __name__ == '__main__':
    make_green_square(Bit.new_bit)
    
