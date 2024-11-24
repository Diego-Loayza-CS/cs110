from byubit import Bit


def reds(bit):
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.move()
    
    
def blues(bit):
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.move()
    
    
def greens(bit):
    bit.paint('green')
    bit.move()
    bit.paint('green')
    bit.move()

    
@Bit.empty_world(5, 3)
def run(bit):
    reds(bit)
    greens(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
