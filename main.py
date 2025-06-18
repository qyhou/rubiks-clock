from clock import Clock


def calc_7_simul_and_print(cl):
    print('=' * 100)
    print(cl.scramble)
    print('=' * 100)
    print(cl.front_state)
    print('-' * 100)
    print(cl.back_state)
    print('=' * 100)
    m1, m2, m3, m4, m5 = cl.get_7_simul_no_flip_tommy_x2()
    print('[7-Simul No-Flip] Tommy Cherry’s Order (x2 encoding): {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.get_7_simul_no_flip_tommy_y2()
    print('[7-Simul No-Flip] Tommy Cherry’s Order (y2 encoding): {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    print('-' * 100)
    m1, m2, m3, m4, m5, m6 = cl.get_7_simul_no_flip_bpaul_x2()
    print('[7-Simul No-Flip] Bpaul’s Order (x2 encoding)       : {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
    m1, m2, m3, m4, m5, m6 = cl.get_7_simul_no_flip_bpaul_y2()
    print('[7-Simul No-Flip] Bpaul’s Order (y2 encoding)       : {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
    print('-' * 100)
    m1, m2, m3, m4, m5 = cl.get_7_simul_flip_tommy_1_x2()
    print('[7-Simul Flip] Tommy Cherry’s Order 1 (x2 encoding) : {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    m1, m2, m3, m4, m5 = cl.get_7_simul_flip_tommy_2_x2()
    print('[7-Simul Flip] Tommy Cherry’s Order 2 (x2 encoding) : {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5))
    print('-' * 100)
    m1, m2, m3, m4, m5, m6 = cl.get_7_simul_flip_bpaul_1_x2()
    print('[7-Simul Flip] Bpaul’s Order 1 (x2 encoding)        : {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
    m1, m2, m3, m4, m5, m6 = cl.get_7_simul_flip_bpaul_2_x2()
    print('[7-Simul Flip] Bpaul’s Order 2 (x2 encoding)        : {}, {}, {}, {}, {}, {}'.format(m1, m2, m3, m4, m5, m6))
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
