from byubit import Bit


def move_to_base(bit):
    while not bit.is_red():
        bit.move()


def paint_trunk(bit):
    while not bit.is_green():
        bit.paint("red")
        bit.move()


@Bit.worlds('fix-tree', 'fix-another-tree')
def fix_the_tree(bit):
    move_to_base(bit)
    bit.left()
    bit.move()
    paint_trunk(bit)


if __name__ == '__main__':
    fix_the_tree(Bit.new_bit)
