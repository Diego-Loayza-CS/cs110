from byubit import Bit


def pallet(bit):
    bit.paint("red")
    bit.move()
    bit.paint("red")


def box(bit):
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.right()
    bit.move()
    bit.paint("blue")
    bit.right()
    bit.move()
    bit.paint("blue")


def face_up(bit):
    bit.left()
    bit.move()
    bit.left()


def start_of_pallet(bit):
    bit.left()
    bit.left()
    bit.move()
    bit.right()
    bit.move()
    bit.right()


@Bit.worlds("boxes")
def stack_boxes(bit):
    pallet(bit)
    face_up(bit)
    box(bit)
    start_of_pallet(bit)
    pallet(bit)
    face_up(bit)
    box(bit)
    start_of_pallet(bit)
    pallet(bit)
    face_up(bit)
    box(bit)
    start_of_pallet(bit)


if __name__ == '__main__':
    stack_boxes(Bit.new_bit)
