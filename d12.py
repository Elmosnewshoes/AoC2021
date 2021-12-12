from pzzl import pzzl
from pprint import pprint
from copy import deepcopy

sections = [x for x in pzzl(12, False).strings()]

def map_caves(sections):
    caves = {}
    for c12 in sections:
        c1, c2 = c12.split('-')
        if c1 not in caves.keys():
            caves[c1] = []
        if c2 not in caves.keys():
            caves[c2] = []
        caves[c1].append(c2)
        caves[c2].append(c1)
    return caves

possible_paths = []

def has_double_visit(path):
    for x in path[1:]:
        if x.islower() and path.count(x) > 1:
            return True
    return False

def find_connecting_sections(path, caves, max_visits = 1):
    paths = []
    for cave in caves[path[-1]]:
        if cave.isupper():
            paths.append(path + tuple([cave, ]))
        elif cave.islower() and not cave == 'start':
            if not cave in path:
                paths.append(path + tuple([cave, ]))
            elif max_visits == 2 and not has_double_visit(path):
                paths.append(path + tuple([cave,]))
    return len(paths), paths

def walk(paths, caves, max_visits = 1):
    new_find = False
    while len(paths) > 0:
        path = paths.pop(0)
        opts, new_paths = find_connecting_sections(path, caves, max_visits)
        if opts > 0:
            new_find = True
            for p in new_paths:
                if p[-1] == 'end':
                    if p[0] == 'start':
                        possible_paths.append(p)
                else:
                    paths.append(p)
    return new_find

caves = map_caves(sections)
paths = [tuple(['start', ])]
new_finds = True
while new_finds:
    new_finds = walk(paths, caves, 2)

print(len(possible_paths))

