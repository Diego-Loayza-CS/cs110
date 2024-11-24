from byubit import Bit

@Bit.worlds('take-cover', 'take-cover2')
def go(bit):
    while bit.left_clear() and bit.right_clear():
        bit.move()
        
go(Bit.new_bit)
