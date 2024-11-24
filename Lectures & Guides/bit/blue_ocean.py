from byubit import Bit


def fill_one_row(bit):
    bit.paint("blue")
    while bit.front_clear():
        bit.move()
        bit.paint("blue")


def go_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.right()

def start(bit):
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.empty_world(6, 6)
def run(bit):
    fill_one_row(bit)
    go_back(bit)
    while bit.left_clear():
        bit.left()
        bit.move()
        bit.right()
        fill_one_row(bit)
        go_back(bit)
    start(bit)

if __name__ == '__main__':
    run(Bit.new_bit)
