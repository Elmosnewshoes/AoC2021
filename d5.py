from copy import deepcopy

with open('input_d5.txt','r') as f:
    raw_input = f.readlines()

raw_input = [x.replace('\n', '') for x in raw_input]

def split_puzzle(inp):
    # split the input in the crates part and move instructions part
    split = inp.index('')
    return inp[:split][::-1], inp[split+1:]


class Pile():
    def __init__(self, ):
        self.stack = ''

    def get(self, n = 1):
        # take n crates off the stack
        crates = self.stack[-n:]
        self.stack = self.stack[:-n]
        return crates

    def put(self, crates):
        # put crates on the stack
        self.stack += crates

    @property
    def top(self,):
        return self.stack[-1]

class CratePiles():
    def __init__(self, init_piles):
        # init_piles is the first part of the input
        pile_string = init_piles[0] # the piles and their index
        pilecount = max([int(x) for x in pile_string if x.isnumeric()])
        self.piles = {i+1: Pile() for i in range(pilecount)}

        for layer in init_piles[1:]:
            # loop the config
            self.add_layer(layer, pile_string)

    def __repr__(self):
        return '\n'.join([f'Pile {i} = {stack.stack}' for i, stack \
                          in self.piles.items()])

    def add_layer(self, layer, pile_string):
        # add a crate on each pile according to config
        for pilenr, crates in self.piles.items():
            ind = pile_string.index(str(pilenr))
            if layer[ind] != ' ':
                self.piles[pilenr].put(layer[ind])

    def move_crate(self, from_pile, to_pile, n = 1):
        crates = self.piles[from_pile].get(n)
        self.piles[to_pile].put(crates)

    def get_top(self,):
        return ''.join([p.top for p in self.piles.values()])


def make_instruction(raw_instruction):
    # convert the instruction lines into numeric instructions
    # return (#reps, from, to)
    x = raw_instruction.replace('move ', '')
    reps, x = x.split(' from ')
    from_pile, to_pile = x.split(' to ')
    return int(reps), int(from_pile), int(to_pile)


def execute_instructions(Piles, instructions, pt = 1):
    for reps, from_pile, to_pile in instructions:
        if pt == 1:
            for _ in range(reps):
                Piles.move_crate(from_pile, to_pile, 1)
        else:
            Piles.move_crate(from_pile, to_pile, reps)

def get_top(piles):
    # read the answer to the puzzle
    res = ''
    for pile, crate in piles.items():
        res += crate[-1]
    return res

init_setup, raw_instructions = split_puzzle(raw_input)

instructions = [make_instruction(instr) for instr in raw_instructions]


PileOfCrates = CratePiles(init_setup)
print(PileOfCrates)
execute_instructions(PileOfCrates, instructions, 1)
print(PileOfCrates.get_top())

PileOfCrates = CratePiles(init_setup)
execute_instructions(PileOfCrates, instructions, 2)
print(PileOfCrates.get_top())
