from pzzl import pzzl
from collections import defaultdict


def apply_actions(polymer, actions):
    output = ''
    for i in range(1, len(polymer)):
        elements = polymer[i-1:i+1]
        if elements in actions.keys():
            output += elements[0] + actions[elements] 
        else:
            output += elements[0]
    output += elements[-1]
    return output

def apply_actions_pt2(polydict, actions, elcount):
    elements = [x for x in polydict.keys() if polydict[x] > 0]
    cur_element_count = {key: val for key, val in polydict.items()}
    for els in elements:
        if els in actions:
            n = cur_element_count[els]
            polydict[els[0] + actions[els]] += n
            polydict[actions[els] + els[1]] += n
            polydict[els] -= n
            elcount[actions[els]] += n

def parse_actions(actions_strings):
    actions = {}
    for rw in actions_strings:
        srch, insrt = rw.split(' -> ')
        actions[srch] = insrt
    return actions

def init_polydict(polymer):
    polydict = defaultdict(int)
    elcount = defaultdict(int)
    for i in range(len(polymer)-1):
        polydict[polymer[i:i+2]] += 1
    for el in polymer:
        elcount[el] += 1
    return polydict, elcount

def calc_score(polymer):
    elements = list(set(polymer))
    scores = [polymer.count(el) for el in elements]
    scores.sort()
    return scores[-1], scores[0]

inp = pzzl(14, False).strings()
start_polymer = inp[0]
actions_strings = inp[1:]
actions = parse_actions(actions_strings)

polymer = start_polymer
steps = 10
for i in range(1,steps + 1):
    polymer = apply_actions(polymer, actions)

mx, mn = calc_score(polymer)
print(mx - mn)

polydict, elcount = init_polydict(start_polymer)
for i in range(40):
    print(f'Round nr {i + 1}')
    apply_actions_pt2(polydict, actions, elcount)
    print(polydict)
    print(elcount, sum(elcount.values()))
element_scores = list(elcount.values())
element_scores.sort()
print(element_scores)
print(element_scores[-1] - element_scores[0], sum(element_scores))
