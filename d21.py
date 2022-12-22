from pzzl import pzzl
from sympy.solvers import solve
from sympy import Symbol

class Primate():
    def __init__(self, init_string):
        self.name, self.op = init_string.split(': ')
        
    def get_equality(self, monkeylist):
        a, _, b = self.op.split(' ')
        try:
            return a.strip(), monkeylist[b.strip()].do_op(monkeylist, True)
        except:
            return b.strip(), monkeylist[a.strip()].do_op(monkeylist, True)

    def get_op(self,monkeylist):
        if self.name == 'humn':
            return 'XXXXX'
        if len(op:=self.op.split(' ')) == 1:
            return str(int(self.op))
        return f'({monkeylist[op[0].strip()].get_op(monkeylist)}\
                    {op[1]} {monkeylist[op[2].strip()].get_op(monkeylist)})'


    def do_op(self, monkeylist, pt2 = False):
        if self.name == 'humn' and pt2:
            raise Exception('Error, human called')
        if len(op:=self.op.split(' ')) == 1:
            return int(self.op)
        return eval(f'int({monkeylist[op[0].strip()].do_op(monkeylist, pt2)}\
                    {op[1]} {monkeylist[op[2].strip()].do_op(monkeylist, pt2)})')


tst = pzzl(21, True).strings()
inp = pzzl(21, ).strings()

# inp = tst

monkeys = {monkey.name: monkey for monkey in {Primate(s) for s in inp}}
print(monkeys['root'].do_op(monkeys, False))
monkey, rhs = monkeys['root'].get_equality(monkeys)
lhs = monkeys[monkey].get_op(monkeys)
XXXXX = Symbol('XXXXX')
print(int(solve(eval(lhs)-rhs, XXXXX)[0]))
