from pzzl import pzzl

cleaning_sections = pzzl(4, ).strings()

def find_bounds(section, q = 1):
    c1, c2 = section.split(',')
    lb1,ub1 = [int(x) for x in c1.split('-')]
    lb2, ub2 = [int(x) for x in c2.split('-')]

    if q == 1:
        if (lb1 <= lb2 and ub1 >= ub2) or \
               (lb2 <= lb1 and ub2 >= ub1)  :
            return 1
    else:
        rng = [0 for i in range(max([ub1,ub2])+1)]
        for i in range(lb1, ub1+1):
            rng[i] = 1
        overlap = sum(rng[lb2: ub2+1])
        if overlap > 0:
            return 1
    return 0

print(sum([find_bounds(x) for x in cleaning_sections]))
print(sum([find_bounds(x, 2) for x in cleaning_sections]))

