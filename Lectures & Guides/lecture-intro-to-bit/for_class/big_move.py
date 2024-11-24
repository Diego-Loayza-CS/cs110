from byubit import Bit


@Bit.empty_world(5,3)
def go(bit):
    bit.paint('green')    
    bit.Move()
    bit.paint('blue')

    
if __name__ == '__main__':
    go(Bit.new_bit)
