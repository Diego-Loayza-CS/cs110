from byubit import Bit


def draw_one_dot(bit):
    bit.turn_left()
    bit.move()
    bit.paint('blue')
    bit.turn_right()
    bit.turn_right()
    bit.move()
    bit.turn_left()


@Bit.empty_world(8, 3)
def dots(bit):
    draw_one_dot(bit)
    bit.move()
    bit.move()
    draw_one_dot(bit)
    bit.move()
    bit.move()
    draw_one_dot(bit)
    bit.move()
    bit.move()
    draw_one_dot(bit)

if __name__ == '__main__':
    dots(Bit.new_bit)
