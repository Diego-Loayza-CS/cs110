from byubit import Bit


def move_to_tree(bit):
    """ Moves to the trunk """
    bit.move()
    bit.move()
    bit.left()


def draw_trunk(bit):
    """ Draws the trunk (two red squares)  """
    bit.paint("red")
    bit.move()
    bit.paint("red")


def draw_branches(bit):
    """ Draws the branches """
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.left()
    bit.move()
    bit.left()
    bit.move()
    bit.paint("green")
    bit.left()
    bit.move()
    bit.move()
    bit.paint("green")


def go_back_down(bit):
    """ Moves back down to the ground, below the right-most branch, facing right. """
    bit.right()
    bit.move()
    bit.move()
    bit.left()


def one_tree(bit):
    move_to_tree(bit)
    draw_trunk(bit)
    draw_branches(bit)
    go_back_down(bit)


@Bit.worlds("trees")
def draw_trees(bit):
    one_tree(bit)
    bit.move()
    one_tree(bit)
    bit.move()
    one_tree(bit)


if __name__ == '__main__':
    draw_trees(Bit.new_bit)
