from pzzl import pzzl
from collections import defaultdict


def apply_actions(polymer, actions):
    """
        Only used for pt1
    """
    output = ''
    for i in range(1, len(polymer)):
        elements = polymer[i-1:i+1]
        if elements in actions.keys():
            output += elements[0] + actions[elements] 
        else:
            output += elements[0]
    output += elements[-1]
    return output

def apply_actions_pt2(element_pairs, actions, elcount):
    """
        element_pairs contains all the pairs of elements in the polymer
        for each pair, create 2 new pairs and update the count
    """
    pairs = [x for x in element_pairs.keys() if element_pairs[x] > 0]
    cur_element_count = {key: val for key, val in element_pairs.items()}
    for pair in pairs:
        if pair in actions:
            n = cur_element_count[pair]
            element_pairs[pair[0] + actions[pair]] += n
            element_pairs[actions[pair] + pair[1]] += n
            element_pairs[pair] -= n
            elcount[actions[pair]] += n

def parse_actions(actions_strings):
    """
        parse the input to a dictionary
        per pair of elements as key, the element that is inserted
    """
    actions = {}
    for rw in actions_strings:
        srch, insrt = rw.split(' -> ')
        actions[srch] = insrt
    return actions

def init_element_pairs(polymer):
    """
        for pt 2
        defaultdict with per element the occurance count in the polymer
        and all the element pairs and the occurance count
    """
    element_pairs = defaultdict(int)
    elcount = defaultdict(int)
    for i in range(len(polymer)-1):
        element_pairs[polymer[i:i+2]] += 1
    for el in polymer:
        elcount[el] += 1
    return element_pairs, elcount

def calc_score(polymer):
    """
        for pt 1 only
        give a sorted list of the frequency occurance per element
        in the polymer
    """
    elements = list(set(polymer))
    scores = [polymer.count(el) for el in elements]
    scores.sort()
    return scores[-1], scores[0]

# INIT
inp = pzzl(14, False).strings()
start_polymer = inp[0]
actions_strings = inp[1:]
actions = parse_actions(actions_strings)
polymer = start_polymer

# PT 1
steps = 10
for i in range(1,steps + 1):
    polymer = apply_actions(polymer, actions)

mx, mn = calc_score(polymer)
print(mx - mn)

# PT 2
element_pairs, elcount = init_element_pairs(start_polymer)
for i in range(40):
    apply_actions_pt2(element_pairs, actions, elcount)
element_scores = list(elcount.values())
element_scores.sort()
print(element_scores[-1] - element_scores[0])
