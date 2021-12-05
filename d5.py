from pzzl import pzzl
import numpy as np


inp = pzzl(5, False).strings()

def parser(lines, diag = False):
    def parse_elements(l):
        def to_int(x):
            return tuple([int(y) for y in x.split(',')])
        return tuple([to_int(l[0]), to_int(l[2])])

    out = [parse_elements(x.split(' ')) for x in lines]
    if diag:
        return out
    return [x for x in out if (x[0][0] == x[1][0] or x[0][1] ==x[1][1])]

class SeaBottom:
    def __init__(self, size = 10):
        self.map = np.zeros((size, size), dtype = int)

    def add_line(self, b, e):
        if (b[0] == e[0] or b[1] == e[1]):
            self.add_horvert_line(b,e)
        else:
            self.add_diag_line(b,e)

    def add_horvert_line(self, b, e):
        x1, x2 = [b[0], e[0]] if b[0] < e[0] else [e[0], b[0]]
        y1, y2 = [b[1], e[1]] if b[1] < e[1] else [e[1], b[1]]
        self.map[y1:y2+1, x1:x2+1] += 1

    def add_diag_line(self, b, e):
        x1, y1 = b
        x2, y2 = e
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        steps = x2-x1 if x2 > x1 else x1-x2
        for i in range(steps+1):
            self.map[y1+i*y_step, x1+i*x_step] += 1

    def return_score(self, thr = 2):
        return np.count_nonzero(self.map >= 2)

    def __str__(self):
        return np.array2string(self.map)


area = SeaBottom(int(1e4))
lines = parser(inp, False)
for line in lines:
    area.add_line(*line)

print(area.return_score(2))

lines2 = parser(inp, True)
area2 = SeaBottom(int(1e4))
for line in lines2:
    area2.add_line(*line)

print(area2.return_score(2))
