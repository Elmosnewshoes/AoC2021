from pzzl import pzzl

tst = [
    "noop",
    "addx 3",
    "addx -5 "]

tst2 = pzzl(10, True).strings()
inp = pzzl(10,).strings()

class Computer():
    def __init__(self,):
        self._x = {0: 1}
        self.cycle = 0
        self.signal = {}

    @property
    def x(self,):
        if self.cycle in self._x.keys():
            return self._x[self.cycle]
        else:
            return self._x[self.cycle-1]

    @x.setter
    def x(self, x):
        self._x[self.cycle] = x

    def next_cycle(self,):
        self.cycle += 1
        self.x = self.x
        self.signal[self.cycle] = self.x * self.cycle

    def add_x(self, dx):
        self._x[self.cycle+1] = self.x + dx

    def calc_increment(self, instr):
        self.next_cycle()
        if 'noop' in instr:
            return
        incr = int(instr.split(' ')[1])
        self.next_cycle()
        self.add_x(incr)

    def get_signal(self,):
        return {i: i*sig for i, sig in self._x.items()}

    def render(self, ):
        lines = []
        for rw in range(6):
            ind = range(rw * 40, (rw+1)*40)
            x = [self._x[i+1] for i in ind]
            lines.append(['x' if val >= i-1 and val <= i + 1 else ' '\
                          for i, val in enumerate(x)])

        for l in lines:
            print(''.join(l))


def loop_instruction(x, handheld):
    for i in x:
        handheld.calc_increment(i)
    return handheld.get_signal()

handheld = Computer()
signal = loop_instruction(inp, handheld)
print(sum([signal[20]] + [signal[i] for i in range(60, 221, 40)]))

handheld.render()


# 14680 is too high
