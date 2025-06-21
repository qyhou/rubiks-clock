from clock import Clock


def calc_7_simul_and_print(cl):
    print('=' * 100)
    print(cl.scramble)
    print('=' * 100)
    print(cl.front_state)
    print('-' * 100)
    print(cl.back_state)
    print('=' * 100)
    m1, m2, m3, m4, m5 = cl.calc_t7s_x2()
    print('T7S x2 encoding: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.calc_t7s_y2()
    print('T7S y2 encoding: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    print('-' * 100)
    m1, m2, m3, m4, m5, m6 = cl.calc_b7s_x2()
    print('B7S x2 encoding: {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
    m1, m2, m3, m4, m5, m6 = cl.calc_b7s_y2()
    print('B7S y2 encoding: {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
    print('-' * 100)
    m1, m2, m3, m4, m5 = cl.calc_t7sf_1()
    print('T7SF Order 1: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.calc_t7sf_2()
    print('T7SF Order 2: {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    print('-' * 100)
    m1, m2, m3, m4, m5, m6 = cl.calc_b7sf_1()
    print('B7SF Order 1: {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
    m1, m2, m3, m4, m5, m6 = cl.calc_b7sf_2()
    print('B7SF Order 2: {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
    print('=' * 100)


def main():
    cl = Clock()
    calc_7_simul_and_print(cl)

    up_gear = input("Input the original scrambled-state position of the gear currently on the U position (U/R/D/L/u/r/d/l): ")
    if up_gear not in ['U', 'R', 'D', 'L', 'u', 'r', 'd', 'l']:
        print('ERROR: invalid position.')

    cl = Clock(scramble=cl.scramble, up_gear=up_gear)
    calc_7_simul_and_print(cl)


if __name__ == '__main__':
    main()
