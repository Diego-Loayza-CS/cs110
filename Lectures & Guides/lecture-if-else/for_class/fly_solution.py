# Solution
from byubit import Bit


def respond_to_square(bit):
    if bit.is_blue():
        bit.left()
    elif bit.is_green():
        bit.right()
        
        
@Bit.worlds('fly')
def run(bit):
    while not bit.is_red():
        respond_to_square(bit)
        bit.move()
        
        
if __name__ == '__main__':
    run(Bit.new_bit)
