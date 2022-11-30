from pzzl import pzzl
import numpy as np

data = pzzl(3, False).strings()
binaries = np.matrix([[int(x) for x in y] for y in data])

length, cols = binaries.shape

ones = binaries.sum(axis = 0)

gamma = ''.join(['1' if (x>length/2) else '0' for x in ones.flat])
epsilon = ''.join(['0' if (x>length/2) else '1' for x in ones.flat])


print(f'ans: gamma * epsilon = {int(gamma,2) * int(epsilon,2)}')

def count(lst, col):
    running_count = 0
    for rw in lst:
        if rw[col] == '1':
            running_count += 1

    if running_count >= len(lst)/2:
        return 1
    return 0

def scrub(lst, crit, col):
    return [rw for rw in lst if rw[col] == str(crit)]

def iter_log(bitflip = 0):
    tmp = data
    col = 0
    while len(tmp) > 1:
        comm_val = count(tmp, col)
        tmp = scrub(tmp, abs(bitflip - comm_val), col)
        col += 1
    return tmp

oxy = iter_log(0)
co2 = iter_log(1)
print(f'Ans pt2 = {int(oxy[0],2) * int(co2[0],2)}')
