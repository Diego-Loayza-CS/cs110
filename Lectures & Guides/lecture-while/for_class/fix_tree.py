from byubit import Bit


@Bit.worlds('fix-tree', 'fix-another-tree')
def fix_the_tree(bit):
    # Implement
    while not bit.is_red():
        bit.move()
    bit.left()
    bit.move()
    while not bit.is_green():
        bit.paint("red")
        bit.move()


if __name__ == '__main__':
    fix_the_tree(Bit.new_bit)
