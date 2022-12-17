from pzzl import pzzl


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, list):
        return compare([left,], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right, ])
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif right < left:
            return -1
        else:
            return 0
    if isinstance(left, list) and isinstance(right, list):
        while left and right:
            l = left.pop(0)
            r = right.pop(0)
            comp = compare(l,r)
            if comp != 0:
                return comp
        if not left and not right:
            return 0
        if not left:
            return 1
        return -1

            


def make_pairs(inp_tuple):
    inp = list(inp_tuple)
    out = {}
    index = 1
    while len(inp)>0:
        out[index] = (
            eval(inp.pop(0)),
            eval(inp.pop(0))
        )
        index += 1
    return out

def loop_compare(pairs):
    rights = []
    for i, pair in pairs.items():
        x = compare(*pair)
        if x == 1:
            rights.append(i)
    return rights

def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst

def sorter(packets):
    while True:
        all_good = 1
        for j in range(len(packets)-1):
            if compare(eval(packets[j]), eval(packets[j+1])) == -1:
                packets = swap(packets, j, j+1)
                all_good = 0
        if all_good == 1:
            return packets

def q2(packets):
    return (1+packets.index('[[2]]')) * (1+packets.index('[[6]]'))

tst = pzzl(13, True).strings()
inp = pzzl(13, ).strings()

pairs = make_pairs(tst)
print(sum(loop_compare(pairs)))

packetlist = list(inp)
packetlist.append('[[2]]')
packetlist.append('[[6]]')
packets = sorter(packetlist)
print(q2(packets))
