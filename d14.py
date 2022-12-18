from pzzl import pzzl
from collections import defaultdict as ddict


class Cave():
    def __init__(self, rock_points):
        x,y = self.find_max(rock_points)
        self.min_row = min(y)
        self.max_row = max(y)
        self.min_col = min(x)
        self.max_col = max(x)
        self.grid = [{} for _ in range(self.max_row + 1)]
        for start, end in rock_points:
            self.make_rock(start,end)

    def eval(self, rw, col):
        # return -1 for rock, or 1 for sand,
        # if not defined in grid, must be open -> return 0
        try:
            X = self.grid[rw]
        except IndexError:
            return 0
        if isinstance(X, ddict):
            return X[col]
        # annoying dict.get overrides defaultdict's default
        return X.get(col, 0)

    def loop(self, col = 500):
        sands = 0
        while self.drop_sand(col):
            sands += 1
            if self.eval(0, 500) == 1:
                # condition: sand source is covered up
                break
        return sands

    def __repr__(self,):
        mapping = {1: 'o', -1: '#' , 0: '.'}
        out = ''
        for i, rw in enumerate(self.grid):
            for x in range(self.min_col, self.max_col+1):
                out+= mapping[self.eval(i, x)]
            out += '\n'
        return out

    def make_rock(self, start, end):
        x0, y0 = start
        x1, y1 = end
        if x0 > x1:
            x1, x0 = x0, x1
        if y0> y1:
            y1, y0 = y0, y1
        for rw in range(y0, y1 + 1):
            for col in range(x0, x1 + 1):
                self.grid[rw][col] = -1

    def drop_sand(self, col = 500, rw = 0):
        if rw > len(self.grid) + 10:
            # the sand has fallen 10 beyond the deepest known depth
            return False
        if self.eval(rw+1, col) == 0:
            return self.drop_sand(col, rw +1)
        if self.eval(rw+1, col-1) == 0:
            return self.drop_sand(col-1, rw+1)
        if self.eval(rw+1, col+1) == 0:
            return self.drop_sand(col+1, rw +1)
        self.grid[rw][col] = 1
        return True

    @staticmethod
    def find_max(points):
        col, rw = zip(*[x[0] for x in points] + [x[1] for x in points])
        return col, rw

def line_to_corners(line):
    coords = line.split(' -> ')
    out = []
    start = coords.pop(0)
    while coords:
        end = coords.pop(0)
        out.append(
            (
                tuple([int(x) for x in start.split(',')]),
                tuple([int(x) for x in end.split(',')])
            )
        )
        start = end
    return out


def make_lines(inp):
    rocks = []
    for ln in inp:
        rocks.extend(line_to_corners(ln))
    return rocks

tst = pzzl(14, True).strings()
inp = pzzl(14,).strings()
coords = make_lines(tst)

cave = Cave(coords)
print(cave.loop())
print(cave)

cave2 = Cave(coords)
cave2.grid.append({})
rockbottom = ddict(lambda: -1)
rockbottom.setdefault(500, -1)
cave2.grid.append(rockbottom) # infinite long layer of rock
print(cave2.loop())
print(cave2)
