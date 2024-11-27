from byubit import Bit


def evaluate_square(bit):
    if bit.is_green() or bit.is_blue():
        bit.paint("red")


@Bit.worlds('red-roses', 'red-roses2')
def run(bit):
    while bit.front_clear():
        evaluate_square(bit)
        bit.move()
    evaluate_square(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
