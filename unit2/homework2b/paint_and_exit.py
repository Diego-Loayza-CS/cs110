from byubit import Bit


def paint_room(bit):
    while not bit.is_blue():
        bit.paint("blue")
        if bit.front_clear():
            bit.move()
        else:
            bit.left()
            bit.move()


def go_to_car(bit):
    while not bit.is_green():
        if bit.front_clear():
            bit.move()
        else:
            bit.right()


@Bit.worlds('paint-and-exit', 'paint-and-exit2')
def run(bit):
    paint_room(bit)
    bit.right()
    go_to_car(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
