from byubit import Bit


def go(bit):
    while bit.front_clear():
        bit.move()


def get_ground_color(bit):
    # Set the marker
    bit.paint('blue')

    # Go to ground
    bit.right()
    go(bit)

    # Get the ground color
    color = bit.get_color()
    bit.snapshot(color)

    # Go back to marker
    bit.left()
    bit.left()
    bit.move()
    while not bit.is_blue():
        bit.move()
    bit.right()

    # Return the color
    return color


def paint_the_cloud(bit):
    color = get_ground_color(bit)
    bit.paint(color)
    bit.snapshot(color)


@Bit.worlds('sky', 'more-sky')
def main(bit):
    while bit.front_clear():
        paint_the_cloud(bit)
        bit.move()
    paint_the_cloud(bit)


if __name__ == '__main__':
    main(Bit.new_bit)
