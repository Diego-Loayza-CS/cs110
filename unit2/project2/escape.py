from byubit import Bit


def pick_up_gem(bit):
    gem_color = bit.get_color()
    bit.erase()
    return gem_color


def found_cliff(bit):
    return bit.is_green()


def trail_until_blocked(bit):
    while bit.front_clear():
        bit.paint("blue")
        bit.move()


def run_through_cave(bit):
    if bit.right_clear():
        bit.right()
    elif bit.left_clear():
        bit.left()
    trail_until_blocked(bit)


def climb_cliff(bit):
    bit.left()
    while bit.is_green():
        bit.move()


def leave_gem(bit, gem):
    bit.right()
    bit.move()
    bit.paint(gem)
    bit.move()


@Bit.worlds('escape', 'escape2')
def run(bit):
    gem = pick_up_gem(bit)
    while not found_cliff(bit):
        run_through_cave(bit)
    climb_cliff(bit)
    leave_gem(bit, gem)


if __name__ == '__main__':
    run(Bit.new_bit)
