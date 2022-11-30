import numpy as np
from pzzl import pzzl

inp = pzzl(1,)
pzzl1 = inp.ints()
diffs = [pzzl1[i] - pzzl1[i-1] for i in range(1,len(pzzl1))]
print(np.sum([1 for x in diffs if x>0]))

# pt 2
pzzl2 = [np.sum(pzzl1[i:i+3]) for i in range(len(pzzl1)-2)]
diffs2 = [pzzl2[i] - pzzl2[i-1] for i in range(1, len(pzzl2))]
print(np.sum([1 for x in diffs2 if x > 0]))
