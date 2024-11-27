from byubit import Bit


def found_gem(bit):
    return not bit.is_empty()


def grab_gem(bit):
    gem_color = bit.get_color()
    bit.erase()
    return gem_color


def enter_pool(bit):
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()
    bit.left()


def paint_row(bit, gem):
    while bit.front_clear():
        bit.paint(gem)
        bit.move()
    bit.paint(gem)


def return_row(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.right()


def next_row(bit):
    bit.right()
    bit.move()
    bit.left()


def paint_pool(bit, gem):
    enter_pool(bit)
    paint_row(bit, gem)
    return_row(bit)
    while bit.right_clear():
        next_row(bit)
        paint_row(bit, gem)
        return_row(bit)


def leave_pool(bit):
    while bit.front_clear():
        bit.move()
    bit.left()
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()


@Bit.worlds('gems', 'gems2')
def run(bit):
    while bit.front_clear():
        bit.move()
        if found_gem(bit):
            gem = grab_gem(bit)
            paint_pool(bit, gem)
            leave_pool(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
