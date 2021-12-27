from pzzl import pzzl
import sys
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple

sys.setrecursionlimit(int(1e4))

class RiskMap:
    def __init__(self, risk_input):
        self.map = [[int(x) for x in y] for y in risk_input]
        self.imax, self.jmax, self.least_risk = self.reinit()
        self.cum_risk = defaultdict(lambda: int(1e99))

    def reinit(self,):
        return len(self.map), len(self.map[0]), \
            int(sum([x[0] for x in self.map]) + sum(self.map[-1]))

    def risk_assessment(self,):
        risk = sum(self.map[0])
        for rw in self.map:
            risk += rw[0]
        return risk


    def eval_map(self, i: int, j: int) -> int:
        return self.map[i][j]


    def adjacents(self, rw, col):
        out = []
        if rw < self.imax - 1:
            out.append((((rw + 1, col),), self.eval_map(rw + 1, col)))
        if col < self.jmax - 1:
            out.append((((rw, col + 1),), self.eval_map(rw, col + 1)))
        if rw > 0:
            out.append((((rw - 1, col),), self.eval_map(rw -1, col)))
        if col > 0:
            out.append((((rw, col - 1),), self.eval_map(rw, col - 1)))
        return out

    def eval_risk(self, steps):
        risk = 0
        for step in steps:
            risk += eval_map(*step)
        return risk

    def walk(self, path, risk):
        """
            This works for pt1 but for pt2 it takes over a day
            to compute :(
        """
        for step, extra_risk in self.adjacents(*path[-1]):
            if step[0] not in path:
                if step[0][0] == self.imax -1 and step[0][1] == self.jmax-1:
                    self.least_risk = min(risk + extra_risk, self.least_risk)
                    print(f'Reduced total risk to {self.least_risk}')
                elif (risk + extra_risk < self.cum_risk[step[0]]
                    and risk + extra_risk < self.least_risk):
                    self.cum_risk[step[0]] = risk+extra_risk
                    self.walk(path + step, risk+extra_risk)



class RiskMap2(RiskMap):
    """
        This class provides a method to accomodate pt2
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def row_plus_one(line):
        def i_plus_one(i):
            return i + 1 if i < 9 else 1
        return [i_plus_one(i) for i in line]

    def expand_map(self, copies = 5):
        new_map = []
        for line in self.map:
            wide_line = line
            tmp_line = line
            for n in range(1,copies):
                tmp_line = self.row_plus_one(tmp_line)
                wide_line += tmp_line
            new_map.append(wide_line)
        i = 0
        while len(new_map) < self.imax*5:
            new_map.append(self.row_plus_one(new_map[i]))
            i += 1
        self.map = new_map
        self.imax, self.jmax, self.least_risk = self.reinit()


class RiskMap3(RiskMap2):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cum_risk = dict()
        self.cum_risks = deepcopy(self.map)


    def adjacents(self, rw, col, risk):
        _adjacents = super().adjacents(rw, col)
        return [(x[0], y + risk) for x,y in _adjacents]

    def walk(self):
        def find_cum_risk(pos):
            adj_risk = self.adjacents(*pos, 0)
            valid_risks = [self.cum_risk[adj] for adj, _ in adj_risk
                           if adj in self.cum_risk.keys()]
            return min(valid_risks) + 10

        start = [((0, 0), 0)]
        self.cum_risk[start[0][0]] = start[0][1]
        self.map[0][0] = 0

        for rw in range(self.imax):
            for col in range(self.jmax):
                pos = (rw, col)
                risk = self.eval_map(*pos)
                if pos != (0, 0):
                    self.find_best_step((pos, risk), find_cum_risk(pos))


    def find_best_step(self, base_step, max_risk) -> None:
        base = base_step[0]
        next_steps = [base_step, ]
        while next_steps:
            cur_loc, cur_risk = next_steps.pop(0)
            for next_loc, next_risk in self.adjacents(*cur_loc, cur_risk):
                if next_loc == base:
                    pass
                elif next_loc in self.cum_risk.keys():
                    risk = self.cum_risk[next_loc] + cur_risk
                    if risk < max_risk:
                        self.cum_risk[base] = risk
                        max_risk = risk
                elif next_risk <= 10:
                    next_steps.append((next_loc, next_risk))
        return None


    def print_cum_risk_map(self,):
        for rw in range(self.imax):
            rwrisk = []
            for col in range(self.jmax):
                rwrisk.append(self.cum_risk[(rw, col)])
            print(rwrisk)

    @property
    def best_risk(self):
        return self.cum_risk[(self.imax - 1, self.jmax - 1)]





risk_input = pzzl(15, False).strings()

Cave = RiskMap3(risk_input)
Cave.walk()
print(f'Best path gives risk {Cave.best_risk}')

Cave2 = RiskMap3(risk_input)
Cave2.expand_map()
Cave2.walk()

print(f'Best path gives risk {Cave2.best_risk}')
