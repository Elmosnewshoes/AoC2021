from pzzl import pzzl


class Cave():
    def __init__(self, rock_points):
        x,y = self.find_max(rock_points)
        self.offset = int(1e6)
        self.min_row = min(y)
        self.max_row = max(y)
        self.min_col = min(x)
        self.max_col = max(x)
        self.grid = [[0 for _ in range(self.max_col + 1 + self.offset)]\
                      for __ in range(self.max_row + 1)]
        for start, end in rock_points:
            self.make_rock(start,end)

    def eval(self, rw, col):
        try:
            return self.grid[rw][col]
        except Exception as e:
            print(f'Couldnt evaluate index {col} at rw {rw}')
            raise e

    def loop(self, col = 500):
        sands = 0
        while self.drop_sand(col):
            sands += 1
            if self.eval(0, 500) == 1:
                break
        return sands

    def __repr__(self,):
        mapping = {1: 'o', -1: '#' , 0: '.'}
        return '\n'.join([''.join([mapping[x] for x in rw[self.offset + self.min_col:]]) \
                for rw in self.grid])

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
        if col+1 > self.max_col or rw + 1 > self.max_row or col-1 < self.min_col:
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
coords = make_lines(inp)

cave = Cave(coords)
print(cave.loop())

max_y = cave.max_row
coords.append(((0,max_y + 2), (1000, max_y + 2)))
cave2 = Cave(coords)
print(cave2.loop())


