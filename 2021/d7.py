from pzzl import pzzl
import numpy as np

def txt_to_input(inp_string):
    return tuple([int(x) for x in inp_string.split(',')])

def max_position(inp_arr):
    return np.max(inp_arr)

def calc_energy_required(positions, x):
    return np.sum(np.absolute(np.array(positions) - x))

def calc_energy_required_2(positions, x, fuel_per_distance):
    # return the fuel cost based on lookup in fuel_per_distance
    return np.sum([fuel_per_distance[dist] for dist in np.absolute(
        np.array(positions) - x, dtype = int)])


def q12(inp_arr):
    # pt1
    positions = list(range(0, max_position(inp_arr) + 1))
    energy_required1 = [calc_energy_required(inp_arr, x) for x in positions]

    # pt2
    # cache fuel cost per distance
    fuel_cost = [np.sum(positions[:i+1]) for i in range(len(positions))]

    energy_required2 = [calc_energy_required_2(inp_arr, x, fuel_cost) for x in positions]
    return np.min(energy_required1), np.min(energy_required2)


# pt 1
inp = txt_to_input(pzzl(7, False).strings()[0])
print(q12(inp))
