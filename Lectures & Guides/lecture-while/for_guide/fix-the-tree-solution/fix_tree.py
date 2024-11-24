from byubit import Bit


def move_to_the_trunk(bit):
    while not bit.is_red():
        bit.move()

    bit.left()


def draw_the_trunk(bit):
    bit.move()
    while not bit.is_green():
        bit.paint('red')
        bit.move()


@Bit.worlds('fix-tree', 'fix-another-tree')
def fix_the_tree(bit):
    move_to_the_trunk(bit)
    draw_the_trunk(bit)


if __name__ == '__main__':
    fix_the_tree(Bit.new_bit)
