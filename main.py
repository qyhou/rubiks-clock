import numpy as np

from clock import Clock

cl = Clock()


def main():
    print(cl.scramble)
    print('=' * 100)
    print(cl.scramble_state_front)
    print('-' * 100)
    print(cl.scramble_state_back)
    print('=' * 100)
    m1, m2, m3, m4, m5 = cl.get_tommy_x2_no_flip(cl.scramble_state)
    print('Tommy x2 no-flip: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.get_tommy_x2_flip(cl.scramble_state)
    print('Tommy x2 flip   : {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.get_tommy_y2_no_flip(cl.scramble_state)
    print('Tommy y2 no-flip: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    print('-' * 100)
    m1, m2, m3, m4, m5 = cl.get_bpaul_x2_no_flip(cl.scramble_state)
    print('Bpaul x2 no-flip: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.get_bpaul_x2_flip(cl.scramble_state)
    print('Bpaul x2 flip   : {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.get_bpaul_y2_no_flip(cl.scramble_state)
    print('Bpaul y2 no-flip: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    print('-' * 100)
    m1, m2, m3, m4 = cl.get_7sfndmw4lm_x2_flip(cl.scramble_state)
    print('7sfndmw4lm x2 flip: {}, {}, {}, {}'.format(m1, m2, m3, m4))


if __name__ == '__main__':
    main()
