from pzzl import pzzl
from typing import List, Tuple


class Map:
    def __init__(self, lines: str) -> None:
        self.heights = tuple([tuple([int(i) for i in line]) for line in lines])
        self.ylim = len(self.heights)
        self.xlim = len(self.heights[0])
        self.minima = []
        self.basins = {}

    def calculate_risk(self, y: int, x: int) -> int:
        return 1 + self.heights[y][x]

    def adjacents(self, y: int, x: int) -> Tuple[Tuple[int]]:
        adjacents = []
        if y > 0:
            adjacents.append((y-1, x))
        if y <= self.ylim -2:
            adjacents.append((y+1, x))
        if x > 0:
            adjacents.append((y, x-1))
        if x <= self.xlim -2:
            adjacents.append((y, x+1))
        return tuple(adjacents)

    def adjacents_basin(self, y: int, x: int) -> Tuple[Tuple[int]]:
        return tuple([yx for yx in self.adjacents(y,x)
                        if self.get_height(*yx) < 9])

    def get_height(self, y: int, x: int) -> int:
        return self.heights[y][x]

    def is_minimal(self, y: int, x: int) -> bool:
        adjacent_values = [self.get_height(*yx) for yx in self.adjacents(y,x)]
        if self.heights[y][x] < min(adjacent_values):
            self.minima.append((y, x))
            self.basins[(y, x)] = []
            return True
        return False

    def find_local_minima(self,) -> List[int]:
        total_risk = []
        for y in range(self.ylim):
            for x in range(self.xlim):
                if self.is_minimal(y, x):
                    total_risk.append(self.calculate_risk(y,x))
        return total_risk

    def find_basins(self, minima_loc: Tuple[int], yx: Tuple[int]):
        for adj_yx in self.adjacents_basin(*yx):
            if adj_yx not in self.basins[minima_loc]:
                self.basins[minima_loc].append(adj_yx)
                self.find_basins(minima_loc, adj_yx)

    def populate_basins(self):
        for yx in self.minima:
            self.find_basins(yx, yx)

    def get_basin_sizes(self)-> List[int]:
        return sorted([len(locs) for locs in self.basins.values()], reverse
                      = True)



inp = pzzl(9, False).strings()
M = Map(inp)
print(sum(M.find_local_minima()))
M.populate_basins()
score = 1
for el in M.get_basin_sizes()[:3]:
    score *= el

print(score)
