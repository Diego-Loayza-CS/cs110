from byubit import Bit


def path_ahead(bit):
    return bit.front_clear()


def found_pool(bit):
    return bit.right_clear()


def enter_pool(bit):
    bit.right()
    bit.move()


def paint_row(bit):
    bit.left()
    bit.paint("blue")
    while bit.front_clear():
        bit.move()
        bit.paint("blue")


def go_back(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.left()


def next_row(bit):
    bit.right()
    bit.move()


def fill_pool(bit):
    while bit.front_clear():
        paint_row(bit)
        go_back(bit)
        bit.snapshot("go_back")
        next_row(bit)
    paint_row(bit)


def leave_pool(bit):
    while bit.front_clear():
        bit.move()
    bit.left()
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()


def build_stem(bit):
    bit.left()
    bit.paint("green")
    bit.move()
    bit.paint("green")


def build_petals(bit):
    bit.left()
    bit.move()
    bit.right()
    bit.move()
    bit.paint("red")
    bit.move()
    bit.right()
    bit.move()
    bit.paint("red")
    bit.right()
    bit.move()
    bit.paint("red")
    bit.left()
    bit.move()
    bit.paint("red")


def plant_flower(bit):
    build_stem(bit)
    build_petals(bit)


def return_to_ground(bit):
    bit.right()
    bit.right()
    bit.move()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('blossoms', 'blossoms2')
def go(bit):
    while path_ahead(bit):
        bit.move()
        if found_pool(bit):
            enter_pool(bit)
            fill_pool(bit)
            leave_pool(bit)
            plant_flower(bit)
            return_to_ground(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
