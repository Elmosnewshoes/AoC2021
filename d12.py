from pzzl import pzzl
from pprint import pprint
from typing import Tuple, List
from collections import defaultdict

def map_caves(sections: List[str]) -> defaultdict:
    """
        Store for each cave, all the adjacent caves
        caves = {
            'start': ['A', 'b'],
            'A': ['start', 'c', 'b', 'd', 'end'],
            ...
            }
    """
    caves = defaultdict(list)
    for c12 in sections:
        c1, c2 = c12.split('-')
        caves[c1].append(c2)
        caves[c2].append(c1)
    return caves


def has_double_visit(path: Tuple[str]) -> bool:
    " Function to check validity of adding cave to path \
    return False when addition of cave to path is permitted "
    for x in path[1:]:
        if x.islower() and path.count(x) > 1:
            " return True if cave is small and already a double visit \
            to a small cave is in the current path "
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


def walk(paths, caves, possible_paths, max_visits = 1):
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


def execute_routefinding(caves: dict, paths: List[tuple],
                         max_visits: int = 2) -> int:
    possible_paths = []
    while walk(paths, caves, possible_paths, max_visits):
        pass
    return len(possible_paths)

sections = [x for x in pzzl(12, False).strings()]
caves = map_caves(sections)

print(execute_routefinding(caves, [tuple(['start', ])], 1))
print(execute_routefinding(caves, [tuple(['start', ])], 2))
