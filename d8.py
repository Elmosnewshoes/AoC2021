from pzzl import pzzl

tst = pzzl(8, True).strings()

def to_ints(inp):
    return [[int(x) for x in ln] for ln in inp]

tst = to_ints(tst)
print(tst)

def check_horizontal(index, inp):
    ln, pos = index
    ubound = len(inp[ln])
    breaker1 = False
    breaker2 = False
    if pos == 0 or pos == ubound-1:
        return True
    tree = inp[ln][pos]
    for i in range(pos + 1, ubound):
        if inp[ln][i] >= tree:
            breaker1 = True
    for i in range(0, pos):
        if inp[ln][i] >= tree:
            breaker2 = True
    if not breaker1 and not breaker2:
        return True
    return False

def check_vertical(index, inp):
    ln, pos = index
    ubound = len(inp)
    breaker1 = False
    breaker2 = False
    if ln == 0 or ln == ubound-1:
        return True
    tree = inp[ln][pos]
    for j in range(ln+1, ubound):
        if inp[j][pos] >= tree:
            breaker1 = True
    for j in range(0,ln):
        if inp[j][pos] >= tree:
            breaker2 = True
    if not breaker1 and not breaker2:
        return True
    return False


def both(index, inp):
    if check_vertical(index, inp) or \
            check_horizontal(index, inp):
        return True
    return False

def loop_all(inp):
    candidates = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if both((i, j), inp):
                candidates.append(1)
    return candidates


print(sum(loop_all(tst)))
