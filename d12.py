from pzzl import pzzl
import heapq
from tqdm import tqdm

class Map():
    def __init__(self, inp):
        self.map = {}
        self.xlim = len(inp[0]) - 1
        self.ylim = len(inp) - 1
        for i, rw in enumerate(inp):
            for j, char in enumerate(rw):
                pos = (i,j)
                if char == 'S':
                    self.start = (i, j)
                    self.map[pos] = ord('a')
                elif char == 'E':
                    self.end = (i, j)
                    self.map[pos] = ord('z')
                else:
                    self.map[pos] = ord(char)
        self.current_paths = []
        self.len = int(1e6) # for pt 2

    def is_reachable(self, one, other):
        if not self.map.get(other, False):
            return False
        if self.map[other] <= self.map[one] + 1:
            return True
        return False

    def adjacents(self, pos):
        y, x = pos
        adjacents = [
            (y-1, x),
            (y+1, x),
            (y, x-1),
            (y, x+1)
        ]
        adjacents = [x for x in adjacents if self.is_reachable(pos, x)]
        if self.end in adjacents:
            return [self.end]
        else:
            return adjacents

    def reset(self, start):
        self.current_paths = []
        self.start = start

    def loop_starting_locations(self, ):
        # This could be a lost marter than brute force (faster)
        starts = [pos for pos, val in self.map.items() if val == ord('a')]
        lengths = []
        for start in tqdm(starts):
            self.reset(start)
            lengths.append(self.meander())
        return min([x for x in lengths if isinstance(x, int)])

    def meander(self,):
        heapq.heappush(self.current_paths, (0, [self.start]))
        places_visited = [self.start]
        while self.current_paths:
            # get the shortest walked path so far
            dist, path = heapq.heappop(self.current_paths)

            #possible next steps
            opts = self.adjacents(path[-1])
            if not opts:
                continue
            if dist > self.len:
                return int(1e6)
            if opts[0] == self.end:
                self.len = dist + 1
                #bc of the sorting, we know this is the shortest direction
                return dist + 1

            for opt in opts:
                if opt not in places_visited:
                    heapq.heappush(self.current_paths, (dist+1, path + [opt]))
                    places_visited.append(opt)



tst = pzzl(12, True).strings()
inp = pzzl(12, ).strings()
forrest = Map(inp)
ln = forrest.meander()
print(ln)
print(forrest.loop_starting_locations())
