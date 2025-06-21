import random
import numpy as np

ROTATE_MAP = {
    'U': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    'R': [2, 8, 14, 15, 9, 3, 1, 7, 13, 16, 10, 4, 0, 6, 12, 17, 11, 5],
    'D': [14, 13, 12, 17, 16, 15, 8, 7, 6, 11, 10, 9, 2, 1, 0, 5, 4, 3],
    'L': [12, 6, 0, 5, 11, 17, 13, 7, 1, 4, 10, 16, 14, 8, 2, 3, 9, 15],
    'u': [3, 4, 5, 0, 1, 2, 9, 10, 11, 6, 7, 8, 15, 16, 17, 12, 13, 14],
    'r': [5, 11, 17, 12, 6, 0, 4, 10, 16, 13, 7, 1, 3, 9, 15, 14, 8, 2],
    'd': [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    'l': [15, 9, 3, 2, 8, 14, 16, 10, 4, 1, 7, 13, 17, 11, 5, 0, 6, 12],
}
STEPS = {
    'UR': np.array([0, 1, 1, -1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    'DR': np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, -1, 0, 0]),
    'DL': np.array([0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, -1]),
    'UL': np.array([1, 1, 0, 0, 0, -1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    'U': np.array([1, 1, 1, -1, 0, -1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    'R': np.array([0, 1, 1, -1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, -1, 0, 0]),
    'D': np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, -1, 0, -1]),
    'L': np.array([1, 1, 0, 0, 0, -1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, -1]),
    '/': np.array([0, 1, 1, -1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, -1]),
    '\\': np.array([1, 1, 0, 0, 0, -1, 1, 1, 1, 0, 0, 0, 0, 1, 1, -1, 0, 0]),
    'ur': np.array([1, 1, 0, 0, 0, -1, 1, 1, 1, 0, 0, 0, 1, 1, 1, -1, 0, -1]),
    'dr': np.array([1, 1, 1, -1, 0, -1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, -1]),
    'dl': np.array([1, 1, 1, -1, 0, -1, 1, 1, 1, 0, 0, 0, 0, 1, 1, -1, 0, 0]),
    'ul': np.array([0, 1, 1, -1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, -1, 0, -1]),
    'ALL': np.array([1, 1, 1, -1, 0, -1, 1, 1, 1, 0, 0, 0, 1, 1, 1, -1, 0, -1])
}

SCRAMBLE_TO_MOVE = {'5-': -5, '4-': -4, '3-': -3, '2-': -2, '1-': -1, '0+': 0,
                 '1+': 1, '2+': 2, '3+': 3, '4+': 4, '5+': 5, '6+': 6}
MOVE_TO_SCRAMBLE = {v: k for k, v in SCRAMBLE_TO_MOVE.items()}

X2_MAP = {'UL': 0, 'U': 1, 'UR': 2, 'dr': 3, 'd': 4, 'dl': 5,
          'L': 6, 'C': 7, 'R': 8, 'r': 9, 'c': 10, 'l': 11,
          'DL': 12, 'D': 13, 'DR': 14, 'ur': 15, 'u': 16, 'ul': 17}
Y2_MAP = {'UL': 0, 'U': 1, 'UR': 2, 'ul': 3, 'u': 4, 'ur': 5,
          'L': 6, 'C': 7, 'R': 8, 'l': 9, 'c': 10, 'r': 11,
          'DL': 12, 'D': 13, 'DR': 14, 'dl': 15, 'd': 16, 'dr': 17}


class Clock(object):
    def __init__(self, scramble=None, up_gear='U'):
        super().__init__()

        self.scramble = scramble
        self.up_gear = up_gear
        self.state = np.array([0 for _ in range(18)])
        self.front_state = None
        self.back_state = None

        self.generate_scramble()
        self.get_state()
        self.rotate()

    def generate_scramble(self):
        if self.scramble is None:
            self.scramble = 'UR{} DR{} DL{} UL{} U{} R{} D{} L{} ALL{} y2 U{} R{} D{} L{} ALL{}'.format(
                *[MOVE_TO_SCRAMBLE[random.randint(-5, 6)] for _ in range(14)])

    def get_state(self):
        front_seq, back_seq = self.scramble.split(' y2 ')
        for s in front_seq.split(' '):
            self.state += STEPS[s[: len(s) - 2]] * SCRAMBLE_TO_MOVE[s[len(s) - 2:]]
        self.state[0: 3], self.state[3: 6], self.state[6: 9], \
            self.state[9: 12], self.state[12: 15], self.state[15: 18] = \
            self.state[3: 6].copy(), self.state[0: 3].copy(), self.state[9: 12].copy(), \
                self.state[6: 9].copy(), self.state[15: 18].copy(), self.state[12: 15].copy()
        for s in back_seq.split(' '):
            self.state += STEPS[s[: len(s) - 2]] * SCRAMBLE_TO_MOVE[s[len(s) - 2:]]
        self.state %= 12
        self.front_state = np.concatenate([self.state[i: i + 3] for i in range(0, len(self.state), 6)]).reshape(3, 3)
        self.back_state = np.concatenate([self.state[i + 3: i + 6] for i in range(0, len(self.state), 6)]).reshape(3, 3)

    def rotate(self):
        self.state = self.state[ROTATE_MAP[self.up_gear]]
        self.front_state = np.concatenate([self.state[i: i + 3] for i in range(0, len(self.state), 6)]).reshape(3, 3)
        self.back_state = np.concatenate([self.state[i + 3: i + 6] for i in range(0, len(self.state), 6)]).reshape(3, 3)

    def calc_t7s_x2(self):
        m1 = -self.state[X2_MAP['d']] + self.state[X2_MAP['c']]
        m2 = (-self.state[X2_MAP['r']] + self.state[X2_MAP['dr']]) + \
             (-self.state[X2_MAP['L']] + self.state[X2_MAP['U']])
        m3 = -self.state[X2_MAP['r']] + self.state[X2_MAP['d']]
        m4 = -((-self.state[X2_MAP['C']] + self.state[X2_MAP['U']]) +
               self.state[X2_MAP['D']] +
               (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']]) +
               (-self.state[X2_MAP['r']] + self.state[X2_MAP['dr']]))
        m5 = (-self.state[X2_MAP['c']] + self.state[X2_MAP['u']]) + \
             self.state[X2_MAP['d']] + \
             (-self.state[X2_MAP['L']] + self.state[X2_MAP['UL']]) + \
             (-self.state[X2_MAP['R']] + self.state[X2_MAP['DR']])
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)

    def calc_t7s_y2(self):
        m1 = -self.state[Y2_MAP['u']] + self.state[Y2_MAP['c']]
        m2 = (-self.state[Y2_MAP['l']] + self.state[Y2_MAP['ul']]) + \
             (-self.state[Y2_MAP['L']] + self.state[Y2_MAP['U']])
        m3 = -self.state[Y2_MAP['l']] + self.state[Y2_MAP['u']]
        m4 = -((-self.state[Y2_MAP['C']] + self.state[Y2_MAP['U']]) +
               self.state[Y2_MAP['D']] +
               (-self.state[Y2_MAP['l']] + self.state[Y2_MAP['ul']]) +
               (-self.state[Y2_MAP['r']] + self.state[Y2_MAP['dr']]))
        m5 = (-self.state[Y2_MAP['c']] + self.state[Y2_MAP['u']]) + \
             self.state[Y2_MAP['d']] + \
             (-self.state[Y2_MAP['L']] + self.state[Y2_MAP['UL']]) + \
             (-self.state[Y2_MAP['R']] + self.state[Y2_MAP['DR']])
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)

    def calc_b7s_x2(self):
        m1 = -self.state[X2_MAP['d']] + self.state[X2_MAP['c']]
        m2 = (-self.state[X2_MAP['r']] + self.state[X2_MAP['dr']]) + \
             (-self.state[X2_MAP['L']] + self.state[X2_MAP['U']])
        m3 = -self.state[X2_MAP['r']] + self.state[X2_MAP['d']]
        m4 = (-self.state[X2_MAP['R']] + self.state[X2_MAP['D']]) + \
             (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']])
        m5 = -self.state[X2_MAP['u']] + self.state[X2_MAP['c']]
        m6 = -self.state[X2_MAP['l']] + self.state[X2_MAP['u']]
        m1, m2, m3, m4, m5, m6 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12, m6 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12, m6 if m6 < 7 else m6 - 12)

    def calc_b7s_y2(self):
        m1 = -self.state[Y2_MAP['u']] + self.state[Y2_MAP['c']]
        m2 = (-self.state[Y2_MAP['l']] + self.state[Y2_MAP['ul']]) + \
             (-self.state[Y2_MAP['L']] + self.state[Y2_MAP['U']])
        m3 = -self.state[Y2_MAP['l']] + self.state[Y2_MAP['u']]
        m4 = (-self.state[Y2_MAP['R']] + self.state[Y2_MAP['D']]) + \
             (-self.state[Y2_MAP['r']] + self.state[Y2_MAP['dr']])
        m5 = -self.state[Y2_MAP['d']] + self.state[Y2_MAP['c']]
        m6 = -self.state[X2_MAP['r']] + self.state[X2_MAP['d']]
        m1, m2, m3, m4, m5, m6 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12, m6 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12, m6 if m6 < 7 else m6 - 12)

    def calc_t7sf_1(self):
        m1 = (-self.state[X2_MAP['DR']] + self.state[X2_MAP['R']]) + \
             (-self.state[X2_MAP['u']] + self.state[X2_MAP['l']])
        m2 = (-self.state[X2_MAP['R']] + self.state[X2_MAP['D']]) + \
             (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']])
        m3 = -self.state[X2_MAP['u']] + self.state[X2_MAP['c']]
        m4 = -((-self.state[X2_MAP['c']] + self.state[X2_MAP['u']]) +
               self.state[X2_MAP['d']] +
               (-self.state[X2_MAP['L']] + self.state[X2_MAP['UL']]) +
               (-self.state[X2_MAP['R']] + self.state[X2_MAP['DR']]))
        m5 = (-self.state[X2_MAP['C']] + self.state[X2_MAP['U']]) + \
             self.state[X2_MAP['D']] + \
             (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']]) + \
             (-self.state[X2_MAP['r']] + self.state[X2_MAP['dr']])
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)

    def calc_t7sf_2(self):
        m1 = (-self.state[X2_MAP['R']] + self.state[X2_MAP['D']]) + \
             (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']])
        m2 = -self.state[X2_MAP['u']] + self.state[X2_MAP['c']]
        m3 = -self.state[X2_MAP['l']] + self.state[X2_MAP['u']]
        m4 = -((-self.state[X2_MAP['c']] + self.state[X2_MAP['u']]) +
               self.state[X2_MAP['d']] +
               (-self.state[X2_MAP['L']] + self.state[X2_MAP['UL']]) +
               (-self.state[X2_MAP['R']] + self.state[X2_MAP['DR']]))
        m5 = (-self.state[X2_MAP['C']] + self.state[X2_MAP['U']]) + \
             self.state[X2_MAP['D']] + \
             (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']]) + \
             (-self.state[X2_MAP['r']] + self.state[X2_MAP['dr']])
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)

    def calc_b7sf_1(self):
        m1 = (-self.state[X2_MAP['DR']] + self.state[X2_MAP['R']]) + \
             (-self.state[X2_MAP['u']] + self.state[X2_MAP['l']])
        m2 = (-self.state[X2_MAP['R']] + self.state[X2_MAP['D']]) + \
             (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']])
        m3 = -self.state[X2_MAP['u']] + self.state[X2_MAP['c']]
        m4 = (-self.state[X2_MAP['r']] + self.state[X2_MAP['d']]) + \
             (-self.state[X2_MAP['L']] + self.state[X2_MAP['UL']])
        m5 = -self.state[X2_MAP['U']] + self.state[X2_MAP['C']]
        m6 = -self.state[X2_MAP['L']] + self.state[X2_MAP['U']]
        m1, m2, m3, m4, m5, m6 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12, m6 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12, m6 if m6 < 7 else m6 - 12)

    def calc_b7sf_2(self):
        m1 = (-self.state[X2_MAP['R']] + self.state[X2_MAP['D']]) + \
             (-self.state[X2_MAP['l']] + self.state[X2_MAP['ul']])
        m2 = -self.state[X2_MAP['u']] + self.state[X2_MAP['c']]
        m3 = -self.state[X2_MAP['l']] + self.state[X2_MAP['u']]
        m4 = (-self.state[X2_MAP['r']] + self.state[X2_MAP['d']]) + \
             (-self.state[X2_MAP['L']] + self.state[X2_MAP['UL']])
        m5 = -self.state[X2_MAP['U']] + self.state[X2_MAP['C']]
        m6 = -self.state[X2_MAP['L']] + self.state[X2_MAP['U']]
        m1, m2, m3, m4, m5, m6 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12, m6 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12, m6 if m6 < 7 else m6 - 12)
