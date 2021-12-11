from pzzl import pzzl
from typing import Tuple, List
import numpy as np


class OctoMap:
    def __init__(self, inp: Tuple[str])->None:
        self.map = np.array([[int(x) for x in ln] for ln in inp])
        self.imax, self.jmax = self.map.shape
        self.flashes = 0


    def adjacents(self, i: int, j: int) -> Tuple[Tuple[int]]:
        adjacents = []
        for ii in range(i-1,i+2):
            if (ii >= 0 and ii < self.imax):
                for jj in range(j-1, j+2):
                    if (jj >= 0 and jj < self.jmax):
                        if not (ii == i and jj == j):
                            adjacents.append((ii, jj))
        return tuple(adjacents)

    def eval_flash(self, i: int, j: int) -> None:
        """ Recursion, evaluate if the octopus indexed by i,j
            flashes, set its value to -1 and evaluate its neighbors """
        if self.map[i][j] >= 10:
            self.flashes += 1
            self.map[i][j] = -1
            for ai, aj in self.adjacents(i, j):
                " Here, evaluate the neighbors "
                if self.map[ai][aj] >= 0:
                    self.map[ai][aj] += 1
                    self.eval_flash(ai, aj)

    def eval_round(self) -> int:
        """ do a hardcoded loop, every octopus gets a val++
            then its flash-condition is evaluated
            at the end of the round, set all flashed octopusses to val -> 0
            return the sum of the map (for pt 2) """

        for i in range(self.imax):
            " Loop over each octopus "
            for j in range(self.jmax):
                if self.map[i][j] >= 0:
                    self.map[i][j] += 1
                    self.eval_flash(i, j)

        " Reset all flashed octopusses and return the sum of the map "
        self.map = np.where(self.map == -1, 0, self.map)
        return np.sum(self.map)

    def __str__(self) -> str:
        return np.array2string(self.map)


Map = OctoMap(pzzl(11, True).strings())
for i in range(100):
    Map.eval_round()
print(Map.flashes)

while Map.eval_round() > 0:
    i += 1
print(i+2)
