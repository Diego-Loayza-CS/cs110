from byubit import Bit


def dance(cosmo):
    cosmo.left()
    cosmo.left()
    cosmo.right()
    cosmo.right()

    
@Bit.empty_world(5, 3)
def run(bit):
    bit.move()
    dance(bit)
    bit.move()
    dance(bit)
    
    
if __name__ == '__main__':
    run(Bit.new_bit)
