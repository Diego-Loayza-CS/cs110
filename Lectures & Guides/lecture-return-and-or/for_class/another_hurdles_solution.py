# Another hurdles solution
# This one is a little trickier than the first
# What happens when the order of if/else conditions is changed (i.e. the not front clear block comes first)?
# Which solution is easier to understand? This one or the other one? Which seems simpler?

from byubit import Bit


def jump(bit):
    bit.left()
    while not bit.right_clear():
        bit.move()
        bit.paint('green')
    bit.right()
    bit.move()
    bit.paint('green')

    
def fall(bit):
    bit.right()
    while bit.front_clear():
        bit.move()
        bit.paint('green')
    bit.left()
    
    
@Bit.run('hurdles', 'more-hurdles')
def run(bit):
    bit.paint('green')
    while bit.left_clear():
        if bit.right_clear():
            fall(bit)

        elif not bit.front_clear():
            jump(bit)
        
        else:
            bit.move()
            bit.paint('green')
            

if __name__ == '__main__':
    run(Bit.new_bit)
    
