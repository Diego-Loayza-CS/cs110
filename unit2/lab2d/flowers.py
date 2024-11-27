from byubit import Bit


def plant_flower(bit, color):
    while not bit.is_green():
        bit.move()
    bit.left()
    while bit.is_green():
        bit.move()
    bit.paint(color)


def return_floor(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.move()


def found_petal(bit):
    return not bit.is_empty()


@Bit.worlds('flowers1', 'flowers2')
def run(bit):
    # Write code here
    while bit.front_clear():
        bit.move()
        if found_petal(bit):
            color = bit.get_color()
            bit.erase()
            plant_flower(bit, color)
            return_floor(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
