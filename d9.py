from pzzl import pzzl

tst = pzzl(9, True).strings()
inp = pzzl(9, ).strings()

tst2 =['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']

def sign(x):
    if x == 0:
        return 0
    return int(x/abs(x))


class Knot():
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        
    def step(self, direction):
        if direction == 'R':
            return self._step(0, 1)
        if direction == 'U':
            return self._step(1, 0)
        if direction == 'L': 
            return self._step(0, -1)
        return self._step(-1, 0)

    def __sub__(self, other):
        return (self.y - other.y, self.x - other.x)
        

    @property
    def pos(self):
        return (self.y, self.x)

    def _step(self, up, right):
        self.x += right
        self.y += up
        return self.pos

class Rope():
    def __init__(self, rope_count = 1):
        self.offset = int(1e6)
        self.knots = [Knot(self.offset, self.offset) for _ in range(rope_count)]
        self.path = [self.knots[-1].pos]


    def parse_instruction(self, ln):
        direction, x = ln.split(' ')
        steps = int(x)
        for _ in range(steps):
            self.knots[0].step(direction)
            for i, knot in enumerate(self.knots[1:]):
                tail_motion = self.calc_catchup(i, i+1)
                for instr in tail_motion:
                    knot.step(instr)
            self.path.append(self.knots[-1].pos)

    def remove_offset(self,):
        return [(y-self.offset, x-self.offset) for y,x in self.path]


    def calc_catchup(self, head_nr, tail_nr):
        dy, dx = self.knots[head_nr] - self.knots[tail_nr]
        instr = []
        if abs(dy) <= 1 and abs(dx) <= 1:
            return []
        if dy > 0: instr.append('U')
        if dy < 0: instr.append('D')
        if dx > 0: instr.append('R')
        if dx < 0: instr.append('L')
        return instr



def loop_soln(inp, knots):
    R = Rope(knots)
    for i in inp:
        R.parse_instruction(i)
    return len(set(R.remove_offset()))

print(loop_soln(inp, 2))
print(loop_soln(inp, 10))
