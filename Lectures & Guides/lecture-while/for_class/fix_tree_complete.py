from byubit import Bit


def go_to_red(bit):
    while not bit.is_red():
        bit.move()
    
    
def paint_to_green(bit):
    # What happens when you do move-then-paint?
    while not bit.is_green():
        bit.paint('red')
        bit.move()
    
    
@Bit.worlds('fix-tree', 'fix-another-tree')
def fix_the_tree(bit):
    # Move Bit to the red square
    go_to_red(bit)
    bit.snapshot('Reached the trunk')
    
    # Fill in the trunk
    bit.left()
    paint_to_green(bit)
    

if __name__ == '__main__':
    fix_the_tree(Bit.new_bit)
