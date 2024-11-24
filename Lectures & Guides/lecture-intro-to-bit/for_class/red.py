from byubit import Bit


@Bit.empty_world(5,3)
def paint_stuff(bit):
    bit.move()
    bit.paint(red)

    
if __name__ == '__main__':
    paint_stuff(Bit.new_bit)
    
