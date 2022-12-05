from pzzl import pzzl

items_list = pzzl(3, ).strings()

def split_item(i):
    l = len(i)
    return (i[:int(l/2)], i[int(l/2):])


def find_common_items(a, b):
    commons = []
    for l in a:
        if l in b and l not in commons:
            commons.append(l)
    return commons

def calc_priority(s):
    if s.isupper():
        return ord(s) - 64 + 26
    return ord(s) - 96

prios = []
for a, b in [split_item(i) for i in items_list]:
    c = find_common_items(a, b)
    prios.append(calc_priority(c[0]))

def find_common_items2(a, b, c):
    for l in a:
        if (l in b) and (l in c):
            return l


def loop_common_items(items):
    commons = []
    for i in range(0, len(items), 3):
        commons.append(find_common_items2(items[i], items[i+1], items[i+2]))
    return commons

print(f'Sum of priorities = {sum(prios)}')
badges = loop_common_items(items_list)
print(f'Sum of priority badges = {sum([calc_priority(x) for x in badges])}')

