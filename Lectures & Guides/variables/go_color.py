from byubit import Bit


def go(bit, color):
    while bit.front_clear():
        bit.move()
        bit.paint(color)
        

@Bit.empty_world(5, 3)
def lots_of_paint(bit):
    go(bit, 'red')
    bit.left()
    go(bit, 'green')
    bit.left()
    go(bit, 'blue')
    

if __name__ == '__main__':
    lots_of_paint(Bit.new_bit)
