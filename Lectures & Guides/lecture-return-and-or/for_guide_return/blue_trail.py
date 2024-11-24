from byubit import Bit


def keep_going(bit):
    if not bit.front_clear():
        return False
    
    elif not bit.is_blue():
        return False
    
    else:
        return True


@Bit.worlds('blue-trail', 'blue-trail2')
def run(bit):
    while keep_going(bit):
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
