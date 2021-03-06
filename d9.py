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
            " When the height is lower than the adjacent heights ... "
            self.minima.append((y, x))  # store the location of the minimum
            self.basins[(y, x)] = []  # initiate a dictionary entry
            return True
        return False

    def find_local_minima(self,) -> List[int]:
        total_risk = []
        for y in range(self.ylim):
            for x in range(self.xlim):
                if self.is_minimal(y, x):
                    total_risk.append(self.calculate_risk(y,x))
        return total_risk

    def expand_basin(self, minima_loc: Tuple[int], yx: Tuple[int]) -> None:
        " Recursion FTW! "
        " Check for an y,x-pair, if it is already in the basin, if not .."
        " .. add it to the basin and run this method on the adjacents "
        " the basin is id-ed by minima_loc (key of dictionary self.basins "
        for adj_yx in self.adjacents_basin(*yx):
            if adj_yx not in self.basins[minima_loc]:
                self.basins[minima_loc].append(adj_yx)
                self.expand_basin(minima_loc, adj_yx)

    def populate_basins(self) -> None:
        " For each minima location, calculate the corresponding basin "
        for yx in self.minima:
            self.expand_basin(yx, yx)

    def get_basin_sizes(self)-> List[int]:
        " Return the size of each basin in sorted order DESC "
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
