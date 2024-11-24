from byubit import Bit


def paint_two(bit, color):
    bit.paint(color)
    bit.move()
    bit.paint(color)
    
    
def paint_three(bit, color):
    paint_two(bit, color)
    bit.move()
    bit.paint(color)
    

@Bit.empty_world(5, 3)
def run(bit):
    first_color = 'red'
    second_color = 'blue'
    
    paint_two(bit, first_color)
    bit.move()
    paint_three(bit, second_color)
    
    bit.left()
    bit.move()
    bit.left()
    
    paint_two(bit, second_color)
    bit.move()
    paint_three(bit, first_color)
    
    
if __name__ == '__main__':
    run(Bit.new_bit)
