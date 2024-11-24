from byubit import Bit


def go(bit, color):
    while bit.front_clear():
        bit.move()
        bit.paint(color)

    
@Bit.worlds('color1', 'color2')
def fill_a_color(bit):
    found_color = bit.get_color()
    go(bit, found_color)
        
        
if __name__ == '__main__':
    fill_a_color(Bit.new_bit)
