from pzzl import pzzl
import numpy as np
from typing import Tuple, List

def parse_input(inp):
    # Split the input in dot locations and fold instructions
    dots = []
    folds = []
    for rw in inp:
        if ',' in rw:
            dots.append([int(i) for i in rw.split(',')])
        elif '=' in rw:
            instr = rw.replace('fold along ', '')
            axis, magn = instr.split('=')
            folds.append([axis, int(magn)])
    return folds, dots


class DotPaper:
    def __init__(self, dots):
       self.imax, self.jmax = self.find_max_input(dots)
       self.paper = np.zeros((self.imax, self.jmax), dtype = int)
       self.populate_paper(dots)

    @staticmethod
    def find_max_input(dots: List[int]) -> Tuple[int]:
        # find the maximum dimension of the paper
        jmax, imax = (0, 0)
        for rw in dots:
            imax = max(imax, rw[1])
            jmax = max(jmax, rw[0])
        return imax + 1, jmax + 1

    def populate_paper(self, dots: List[Tuple[int]]) -> None:
        # print a dot (1) on the paper
        for j,i in dots:
            self.paper[i][j] = 1

    def fold(self, axis: str, magn: int) -> None:
        # fold the paper and shrink the paper size to the place of the fold
        if axis == 'x':
            # vertical fold
            for i in range(self.imax ):
                for j in range(self.jmax - magn):
                    self.paper[i][magn - j] += self.paper[i][magn + j]
            self.jmax = magn

        elif axis == 'y':
            # horizontal fold
            for j in range(self.jmax ):
                for i in range(self.imax - magn):
                    self.paper[magn - i][j] += self.paper[i + magn][j]
            self.imax = magn

        # shrink the paper to new dimensions
        self.paper = self.paper[:self.imax,:self.jmax]

folds, dots = parse_input(pzzl(13, False).strings())
DP = DotPaper(dots)
DP.fold(*folds[0])
print(f'After 1 fold: {np.count_nonzero(DP.paper)} dots')


for instr in folds[1:]:
    DP.fold(*instr)

# do some manipulation for readability
for rw in np.where(DP.paper > 0, 1, DP.paper):
    print(''.join([str(x) for x in rw]).replace('0',' '))
