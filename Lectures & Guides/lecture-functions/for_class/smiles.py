from byubit import Bit


def triple_blue(block):
    block.paint("blue")
    block.move()
    block.paint("blue")
    block.move()
    block.paint("blue")
    block.move()


def blue_smile(tilin):
    tilin.move()
    tilin.paint("blue")
    tilin.right()
    tilin.move()
    tilin.move()
    tilin.paint("blue")
    tilin.move()
    tilin.left()
    tilin.move()
    triple_blue(tilin)
    tilin.left()
    tilin.move()
    tilin.paint("blue")
    tilin.move()
    tilin.move()
    tilin.paint("blue")
    tilin.right()


@Bit.worlds('smiles')
def run(triangle):
    blue_smile(triangle)
    triangle.move()
    blue_smile(triangle)
    triangle.move()
    blue_smile(triangle)
    triangle.move()
    blue_smile(triangle)


if __name__ == '__main__':
    run(Bit.new_bit)
