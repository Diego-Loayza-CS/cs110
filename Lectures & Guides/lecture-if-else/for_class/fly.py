from byubit import Bit


def evaluate_square(bit):
    if bit.is_green():
        bit.right()

    elif bit.is_blue():
        bit.left()


@Bit.worlds('fly')
def run(bit):
    while not bit.is_red():
        evaluate_square(bit)
        bit.move()
        bit.snapshot("movement")


if __name__ == '__main__':
    run(Bit.new_bit)
