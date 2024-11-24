from byubit import Bit


def spin(bit):
    """
    Spins Bit 360 degrees
    
    Bit ends facing the same direction as the start.
    """
    bit.left()
    bit.left()
    bit.left()
    bit.left()
    
    
@Bit.empty_world(5, 3)
def run(bit):
    spin(bit)
    bit.move()
    spin(bit)

    
if __name__ == '__main__':
    run(Bit.new_bit)
