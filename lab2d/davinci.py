from byubit import Bit

# This change lets us draw really big pictures
import byubit

byubit.bit.MAX_STEP_COUNT = 10_000


def go_paint(bit, color):
    """Paint `color` until blocked in front"""
    while bit.can_move_front():
        bit.paint(color)
        bit.move()


def run(bit, how_many):
    """Move bit `how_many` squares"""
    if how_many > 0:
        bit.move()
        run(bit, how_many - 1)


def paint_many(bit, color, how_many):
    """Paint `color` and move `how_many` times"""
    if how_many > 0:
        bit.paint(color)
        bit.move()
        paint_many(bit, color, how_many - 1)


def paint_to(bit, color, ending_color):
    """Paint `color` until you reach `ending_color`"""
    while bit.get_color() != ending_color:
        bit.paint(color)
        bit.move()


def box(bit, color, size):
    """
    Draws a box of the specified color and size
    Bit starts and ends in the same position and orientation
    Bit expects that the starting square is not already the specified color
    """
    while bit.get_color() != color:
        paint_many(bit, color, size)
        bit.turn_left()


def turn_around(bit):
    bit.turn_left()
    bit.turn_left()


def go(bit):
    """Go until blocked in front"""
    while bit.can_move_front():
        bit.move()


def column(bit, color):
    """Fill a column with `color`"""
    bit.turn_left()
    go_paint(bit, color)
    turn_around(bit)
    go_paint(bit, color)
    bit.turn_left()


def fill(bit, color):
    """Fill the unblocked space with `color`"""
    column(bit, color)
    while bit.can_move_front():
        bit.move()
        column(bit, color)


@Bit.empty_world(14, 12)
def draw(bit):
    run(bit, 2)
    paint_many(bit, "black", 3)
    run(bit, 4)
    paint_many(bit, "black", 3)
    bit.left()
    bit.move()
    bit.paint("black")
    bit.right()
    bit.move()
    bit.left()
    bit.move()
    paint_many(bit, "black", 7)
    bit.left()
    bit.move()
    bit.right()
    paint_many(bit, "black", 2)
    bit.left()
    bit.move()
    paint_many(bit, "black", 3)
    bit.left()
    bit.move()
    bit.right()
    paint_many(bit, "black", 4)
    bit.right()
    bit.move()
    bit.left()
    paint_many(bit, "black", 3)
    bit.left()
    bit.move()
    paint_many(bit, "black", 2)
    bit.right()
    bit.move()
    bit.left()
    paint_many(bit, "black", 7)
    bit.left()
    bit.move()
    bit.paint("black")
    run(bit, 4)
    paint_many(bit, "black", 4)
    run(bit, 2)
    bit.left()
    run(bit, 6)
    box(bit, "pink", 1)
    run(bit, 2)
    bit.left()
    bit.move()
    bit.paint("black")
    run(bit, 2)
    bit.left()
    bit.move()
    bit.paint("black")
    bit.move()
    bit.right()
    bit.move()
    paint_many(bit, "black", 2)
    bit.right()
    bit.move()
    bit.paint("black")
    bit.move()
    bit.left()
    run(bit, 2)
    bit.paint("black")
    bit.move()
    bit.left()
    bit.move()
    box(bit, "pink", 1)


if __name__ == '__main__':
    draw(Bit.new_bit)
