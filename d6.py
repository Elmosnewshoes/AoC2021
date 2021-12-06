from pzzl import pzzl
from typing import Tuple
import numpy as np


def compute_next_generation(gen):
    gen_arr = np.array(gen, dtype = int)
    zeros = gen_arr.size - np.count_nonzero(gen_arr)
    gen_arr -= 1
    gen_arr = np.where(gen_arr < 0, 6, gen_arr)
    return tuple(gen_arr) + tuple(np.ones(zeros, dtype = int) * 8)


def smart_compute_next_generation(ages):
    zeros = ages[0]
    for i in range(8):
        ages[i] = ages[i+1]

    ages[8] = zeros
    ages[6] = ages[6] + zeros
    return ages


gen = tuple([int(i) for i in pzzl(6, True).strings()[0].split(',')])
for i in range(80):
    gen = compute_next_generation(gen)

print('Answer for pt 1: ', len(gen))

gen_count = [ 0 for i in range(9)]
start_pop = [int(i) for i in pzzl(6, False).strings()[0].split(',')]
for el in start_pop:
    gen_count[el] = gen_count[el] + 1

print(gen_count)
for i in range(256):
    gen_count = smart_compute_next_generation(gen_count)

print('Answer for pt 2: ', np.sum(gen_count))
