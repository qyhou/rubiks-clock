import random
import numpy as np


class Clock(object):
    def __init__(self, scramble=None):
        super().__init__()

        self.steps = {
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
        self.scramble2move = {'5-': -5, '4-': -4, '3-': -3, '2-': -2, '1-': -1, '0+': 0,
                              '1+': 1, '2+': 2, '3+': 3, '4+': 4, '5+': 5, '6+': 6}
        self.move2scramble = {v: k for k, v in self.scramble2move.items()}
        self.y2_map = {'UL': 0, 'U': 1, 'UR': 2, 'ul': 3, 'u': 4, 'ur': 5,
                       'L': 6, 'C': 7, 'R': 8, 'l': 9, 'c': 10, 'r': 11,
                       'DL': 12, 'D': 13, 'DR': 14, 'dl': 15, 'd': 16, 'dr': 17}
        self.x2_map = {'UL': 0, 'U': 1, 'UR': 2, 'dr': 3, 'd': 4, 'dl': 5,
                       'L': 6, 'C': 7, 'R': 8, 'r': 9, 'c': 10, 'l': 11,
                       'DL': 12, 'D': 13, 'DR': 14, 'ur': 15, 'u': 16, 'ul': 17}

        self.scramble = self.generate_scramble(scramble)

        self.scramble_state, self.scramble_state_front, self.scramble_state_back = self.calc_scramble_state(self.scramble)
        
    
    def generate_scramble(self, scramble):
        if scramble is None:
            scramble = 'UR{} DR{} DL{} UL{} U{} R{} D{} L{} ALL{} y2 U{} R{} D{} L{} ALL{}'.format(
                *[self.move2scramble[random.randint(-5, 6)] for _ in range(14)])
        return scramble
    
    def calc_scramble_state(self, scramble):
        state = np.array([0 for _ in range(18)])
        front_seq, back_seq = scramble.split(' y2 ')
        for s in front_seq.split(' '):
            state += self.steps[s[: len(s) - 2]] * self.scramble2move[s[len(s) - 2:]]
        state[0: 3], state[3: 6], state[6: 9], state[9: 12], state[12: 15], state[15: 18] = \
            state[3: 6].copy(), state[0: 3].copy(), state[9: 12].copy(), \
                state[6: 9].copy(), state[15: 18].copy(), state[12: 15].copy()
        for s in back_seq.split(' '):
            state += self.steps[s[: len(s) - 2]] * self.scramble2move[s[len(s) - 2:]]
        state %= 12
        scramble_state = state
        scramble_state_front = np.concatenate([state[i: i + 3] for i in range(0, len(state), 6)]).reshape(3, 3)
        scramble_state_back = np.concatenate([state[i + 3: i + 6] for i in range(0, len(state), 6)]).reshape(3, 3)
        return scramble_state, scramble_state_front, scramble_state_back
    
    def get_tommy_x2_no_flip(self, scramble_state):
        m1 = -scramble_state[self.x2_map['d']] + scramble_state[self.x2_map['c']]
        m2 = (-scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['dr']]) + \
             (-scramble_state[self.x2_map['L']] + scramble_state[self.x2_map['U']])
        m3 = -scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['d']]
        m4 = -((-scramble_state[self.x2_map['C']] + scramble_state[self.x2_map['U']]) +
             scramble_state[self.x2_map['D']] +
             (-scramble_state[self.x2_map['l']] + scramble_state[self.x2_map['ul']]) +
             (-scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['dr']]))
        m5 = (-scramble_state[self.x2_map['c']] + scramble_state[self.x2_map['u']]) + \
             scramble_state[self.x2_map['d']] + \
             (-scramble_state[self.x2_map['L']] + scramble_state[self.x2_map['UL']]) + \
             (-scramble_state[self.x2_map['R']] + scramble_state[self.x2_map['DR']])
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12, 
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)

    def get_tommy_x2_flip(self, scramble_state):
        m1 = (-scramble_state[self.x2_map['DR']] + scramble_state[self.x2_map['R']]) + \
             (-scramble_state[self.x2_map['u']] + scramble_state[self.x2_map['l']])
        m2 = (-scramble_state[self.x2_map['R']] + scramble_state[self.x2_map['D']]) + \
             (-scramble_state[self.x2_map['l']] + scramble_state[self.x2_map['ul']])
        m3 = -scramble_state[self.x2_map['u']] + scramble_state[self.x2_map['c']]
        m4 = -((-scramble_state[self.x2_map['c']] + scramble_state[self.x2_map['u']]) +
             scramble_state[self.x2_map['d']] +
             (-scramble_state[self.x2_map['L']] + scramble_state[self.x2_map['UL']]) +
             (-scramble_state[self.x2_map['R']] + scramble_state[self.x2_map['DR']]))
        m5 = (-scramble_state[self.x2_map['C']] + scramble_state[self.x2_map['U']]) + \
             scramble_state[self.x2_map['D']] + \
             (-scramble_state[self.x2_map['l']] + scramble_state[self.x2_map['ul']]) + \
             (-scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['dr']])
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)
    
    def get_tommy_y2_no_flip(self, scramble_state):
        m1 = -scramble_state[self.y2_map['u']] + scramble_state[self.y2_map['c']]
        m2 = (-scramble_state[self.y2_map['l']] + scramble_state[self.y2_map['ul']]) + \
             (-scramble_state[self.y2_map['L']] + scramble_state[self.y2_map['U']])
        m3 = -scramble_state[self.y2_map['l']] + scramble_state[self.y2_map['u']]
        m4 = -((-scramble_state[self.y2_map['C']] + scramble_state[self.y2_map['U']]) +
             scramble_state[self.y2_map['D']] +
             (-scramble_state[self.y2_map['l']] + scramble_state[self.y2_map['ul']]) +
             (-scramble_state[self.y2_map['r']] + scramble_state[self.y2_map['dr']]))
        m5 = (-scramble_state[self.y2_map['c']] + scramble_state[self.y2_map['u']]) + \
             scramble_state[self.y2_map['d']] + \
             (-scramble_state[self.y2_map['L']] + scramble_state[self.y2_map['UL']]) + \
             (-scramble_state[self.y2_map['R']] + scramble_state[self.y2_map['DR']])
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12, 
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)
    
    def get_bpaul_x2_no_flip(self, scramble_state):
        m1 = -scramble_state[self.x2_map['d']] + scramble_state[self.x2_map['c']]
        m2 = (-scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['dr']]) + \
             (-scramble_state[self.x2_map['L']] + scramble_state[self.x2_map['U']])
        m3 = -scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['d']]
        m4 = (-scramble_state[self.x2_map['R']] + scramble_state[self.x2_map['D']]) + \
             (-scramble_state[self.x2_map['l']] + scramble_state[self.x2_map['ul']])
        m5 = -scramble_state[self.x2_map['u']] + scramble_state[self.x2_map['c']]
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12, 
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)
    
    def get_bpaul_x2_flip(self, scramble_state):
        m1 = (-scramble_state[self.x2_map['DR']] + scramble_state[self.x2_map['R']]) + \
             (-scramble_state[self.x2_map['u']] + scramble_state[self.x2_map['l']])
        m2 = (-scramble_state[self.x2_map['R']] + scramble_state[self.x2_map['D']]) + \
             (-scramble_state[self.x2_map['l']] + scramble_state[self.x2_map['ul']])
        m3 = -scramble_state[self.x2_map['u']] + scramble_state[self.x2_map['c']]
        m4 = (-scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['d']]) + \
             (-scramble_state[self.x2_map['L']] + scramble_state[self.x2_map['UL']])
        m5 = -scramble_state[self.x2_map['U']] + scramble_state[self.x2_map['C']]
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)
    
    def get_bpaul_y2_no_flip(self, scramble_state):
        m1 = -scramble_state[self.y2_map['u']] + scramble_state[self.y2_map['c']]
        m2 = (-scramble_state[self.y2_map['l']] + scramble_state[self.y2_map['ul']]) + \
             (-scramble_state[self.y2_map['L']] + scramble_state[self.y2_map['U']])
        m3 = -scramble_state[self.y2_map['l']] + scramble_state[self.y2_map['u']]
        m4 = (-scramble_state[self.y2_map['R']] + scramble_state[self.y2_map['D']]) + \
             (-scramble_state[self.y2_map['r']] + scramble_state[self.y2_map['dr']])
        m5 = -scramble_state[self.y2_map['d']] + scramble_state[self.y2_map['c']]
        m1, m2, m3, m4, m5 = m1 % 12, m2 % 12, m3 % 12, m4 % 12, m5 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12, 
                m4 if m4 < 7 else m4 - 12, m5 if m5 < 7 else m5 - 12)

    def get_7sfndmw4lm_x2_flip(self, scramble_state):
        m1 = (-scramble_state[self.x2_map['R']] + scramble_state[self.x2_map['D']]) + \
             (-scramble_state[self.x2_map['l']] + scramble_state[self.x2_map['ul']])
        m2 = -scramble_state[self.x2_map['u']] + scramble_state[self.x2_map['c']]
        m3 = -scramble_state[self.x2_map['l']] + scramble_state[self.x2_map['u']]
        m4 = (-scramble_state[self.x2_map['r']] + scramble_state[self.x2_map['d']]) + \
             (-scramble_state[self.x2_map['L']] + scramble_state[self.x2_map['UL']])
        m1, m2, m3, m4 = m1 % 12, m2 % 12, m3 % 12, m4 % 12
        return (m1 if m1 < 7 else m1 - 12, m2 if m2 < 7 else m2 - 12, m3 if m3 < 7 else m3 - 12,
                m4 if m4 < 7 else m4 - 12)
