from math import floor
from pzzl import pzzl

class Item():
    is_divisible_opts = []

    def __init__(self, level):
        self.level = level
        self.is_divisible_by = {}
        self.op = None
        self.x = None

    def prime(self, ):
        self.is_divisible_by = {i: self.level % i for i in \
                                self.is_divisible_opts}

    def new_level(self, operation, x=None):
        self.x = x
        self.op = operation
        if operation == '*':
            self.multiply_level(x)
        elif operation == '+':
            self.add_level(x)
        else:
            self.square_level()

    def check_condition(self, x):
        return self.is_divisible_by[x] == 0

    def add_level(self, increment):
        self.is_divisible_by = {i: (val + increment) % i for i, val in
                                self.is_divisible_by.items()}
    def multiply_level(self, factor):
        self.is_divisible_by = {i: (val * factor) % i for i, val in
                                self.is_divisible_by.items()}

    def square_level(self):
        self.is_divisible_by = {i: (val * val) % i for i, val in
                                self.is_divisible_by.items()}

    def parse_relief(self, division):
        if self.op == '*':
            self.level *= self.x
        elif self.op == '+':
            self.level += self.x
        else:
            self.level *= self.level
        self.level = floor(self.level/division)
        self.prime()

    def __repr__(self,):
        return str(self.level)


class Monkey():
    def __init__(self, starting_items, operation, test, recipients):
        self.items = [Item(int(x)) for x in
                      starting_items.replace('Starting items: ', '')
                      .split(',')]
        if '+' in operation:
            self.operation = ('+', int(operation.split(' ')[-1]))
        elif 'old * old' in operation:
            self.operation = ('**', None)
        else:
            self.operation = ('*', int(operation.split(' ')[-1]))
        self.test = int(test.replace('Test: divisible by ', ''))
        self.monkey_true = int(recipients[0].
                               replace('If true: throw to monkey ', ''))
        self.monkey_false = int(recipients[1].
                                replace('If false: throw to monkey ', ''))
        self.inspections = 0

    def calc_recipient(self, item):
        if item.check_condition(self.test):
            return self.monkey_true
        return self.monkey_false

    def receive(self, item):
        self.items.append(item)

    def throw_list(self, relief=3):
        return [x for x in self.inspect_and_throw(relief)]

    def inspect_and_throw(self, relief):
        while len(self.items) > 0:
            self.inspections += 1
            item = self.items.pop(0)
            item.new_level(*self.operation)
            if relief == 3:
                item.parse_relief(relief)
            yield self.calc_recipient(item), item


def make_monkeys(input_tuple):
    inp = list(input_tuple)
    divisions = []
    monkeys = []
    while len(inp) > 0:
        if inp[0] == '' or 'Monkey ' in inp[0]:
            _ = inp.pop(0)
            continue
        items = inp.pop(0)
        op = inp.pop(0)
        test = inp.pop(0)
        recipients = (inp.pop(0), inp.pop(0))
        monkeys.append(Monkey(items, op, test, recipients))
        Item.is_divisible_opts.append(monkeys[-1].test)
    for m in monkeys:
        for i in m.items:
            i.prime()
    return monkeys


def rounds(monkeys, n, relief=3):
    for _ in range(n):
        for monkey in monkeys:
            throw_list = monkey.throw_list(relief)
            for ind, item in throw_list:
                monkeys[ind].receive(item)
    return monkeys


def q1(monkeys):
    monkey_business = [m.inspections for m in monkeys]
    monkey_business.sort()
    return monkey_business[-1] * monkey_business[-2], monkey_business


inp = pzzl(11, False).strings()
tst = pzzl(11, True).strings()
monkeys = make_monkeys(tst)
monkeys = rounds(monkeys, 20, 3)
print(q1(monkeys))

monkeys = make_monkeys(inp)
monkeys = rounds(monkeys, 10000, 1)
print(q1(monkeys))
