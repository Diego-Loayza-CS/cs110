from byubit import Bit


def plant_mark(bit):
    bit.paint("blue")


def go_down(bit):
    bit.right()
    while bit.front_clear():
        bit.move()


def turn_around(bit):
    bit.left()
    bit.left()


def paint_cloud(bit, color):
    bit.move()
    while not bit.is_blue():
        bit.move()
    bit.paint(color)
    bit.right()


@Bit.worlds('sky', 'more-sky')
def main(bit):
    plant_mark(bit)
    go_down(bit)
    cloud = bit.get_color()
    turn_around(bit)
    paint_cloud(bit, cloud)
    while bit.front_clear():
        bit.move()
        plant_mark(bit)
        go_down(bit)
        cloud = bit.get_color()
        turn_around(bit)
        paint_cloud(bit, cloud)


if __name__ == '__main__':
    main(Bit.new_bit)
