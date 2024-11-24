# Solution
from byubit import Bit, use_text_renderer
use_text_renderer()

def respond_to_square(bit):
    if bit.is_blue():
        bit.left()
    elif bit.is_green():
        bit.right()
        
        
@Bit.worlds('for_class/worlds/fly')
@Bit.pictures('images/', ext='svg', title='Fly!')
def run(bit):
    while not bit.is_red():
        respond_to_square(bit)
        bit.move()
        
        
if __name__ == '__main__':
    run(Bit.new_bit)
