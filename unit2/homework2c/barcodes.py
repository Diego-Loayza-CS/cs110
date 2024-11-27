from byubit import Bit


def found_barcode(bit):
    return bit.is_blue()


def paint_barcode(bit):
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint("blue")


def return_ground(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def create_barcode(bit):
    paint_barcode(bit)
    return_ground(bit)


@Bit.worlds('barcode', 'barcode2')
def run(bit):
    if found_barcode(bit):
        create_barcode(bit)
    while bit.front_clear():
        bit.move()
        if found_barcode(bit):
            create_barcode(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
