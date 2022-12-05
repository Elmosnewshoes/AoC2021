from copy import deepcopy

with open('input_d5.txt','r') as f:
    raw_input = f.readlines()

raw_input = [x.replace('\n', '') for x in raw_input]

def split_puzzle(inp):
    # split the input in the crates part and move instructions part
    split = inp.index('')
    return inp[:split][::-1], inp[split+1:]

def compose_pile(pile_string, piles, layer):
    # parse a line from the crates part of the puzzle input
    new_piles = piles
    for pile, crates in piles.items():
        ind = pile_string.index(str(pile))
        if layer[ind] != ' ':
            new_piles[pile] = crates + layer[ind]
    return new_piles

def make_starting_pile(init_piles):
    # get a dictionary indexed by pile number
    # each pile is a string with crate letters
    # return the dictionary {1: 'ZN', 2: 'MCD' ..}
    pile_string = init_piles[0]
    pilecount = max([int(x) for x in pile_string if x.isnumeric()])
    piles = {i+1: '' for i in range(pilecount)}
    for layer in init_piles[1:]:
        piles = compose_pile(pile_string, piles, layer)
    return piles


def make_instruction(raw_instruction):
    # convert the instruction lines into numeric instructions
    # return (#reps, from, to)
    x = raw_instruction.replace('move ', '')
    reps, x = x.split(' from ')
    from_pile, to_pile = x.split(' to ')
    return int(reps), int(from_pile), int(to_pile)

def move_crate(from_pile, to_pile, piles, n = 1):
    # execute a single instruction on the pile dictionary
    # return the newly formed pile dictionary
    crates = piles[from_pile][-n:]
    piles[from_pile] = piles[from_pile][:-n]
    piles[to_pile] = piles[to_pile] + crates
    return piles

def loop_instructions(piles, instructions, pt = 1):
    # execute the move_crate for each consecutive instruction
    for reps, from_pile, to_pile in instructions:
        if pt == 1:
            for _ in range(reps):
                piles = move_crate(from_pile, to_pile, piles)
        else:
            piles = move_crate(from_pile, to_pile, piles, reps)
    return piles

def get_top(piles):
    # read the answer to the puzzle
    res = ''
    for pile, crate in piles.items():
        res += crate[-1]
    return res
        

init_setup, raw_instructions = split_puzzle(raw_input)

piles = make_starting_pile(init_setup)
print(piles)
instructions = [make_instruction(instr) for instr in raw_instructions]

result = loop_instructions(piles, instructions)

print(get_top(result))
piles2 = make_starting_pile(init_setup)
result2 = loop_instructions(piles2, instructions, pt = 2)
print(get_top(result2))
