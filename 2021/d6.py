from pzzl import pzzl
from typing import Tuple
import numpy as np

def smart_compute_next_generation(ages):
    zeros = ages[0]
    for i in range(8):
        ages[i] = ages[i+1]

    ages[8] = zeros
    ages[6] = ages[6] + zeros
    return ages

gen_count = [ 0 for i in range(9)]
start_pop = [int(i) for i in pzzl(6, False).strings()[0].split(',')]
for el in start_pop:
    # count the population per bin
    gen_count[el] = gen_count[el] + 1

for i in range(256):
    gen_count = smart_compute_next_generation(gen_count)
    if i == 79:
        print('Answer for pt 1: ', np.sum(gen_count))

print('Answer for pt 2: ', np.sum(gen_count))
