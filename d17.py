from pzzl import pzzl

def inp_to_pars(inp):
    def to_int(x):
        return [int(i) for i in x[2:].split('..')]
    xx, yy = inp.split(', ')
    return to_int(xx), to_int(yy)

def vminx(xmin):
    vmin = 0
    while sum(range(vmin+1)) < xmin:
        vmin += 1
    return vmin

def simulate(vx0, vy0, ymin, ymax, xmin, xmax):
    y = 0
    x = 0
    traj = [(0,0), ]
    vy = vy0
    vx = vx0
    valid = False
    while y >= ymin and x <= xmax:
        y += vy
        x += vx
        vy -= 1
        vx = vx-1 if vx > 0 else 0
        traj.append((x, y))
        if y >= ymin and y <= ymax and x>= xmin and x<= xmax:
            valid = True
    return traj, valid


def calc_height(ymin, ymax, xmin):
    best_traj = []
    trajectories = []
    for vy0 in range(ymin,10):
        traj, isok = simulate(0, vy0, ymin, int(1e99), xmin, int(1e99))
        if isok:
            best_traj = traj
            print(traj)
            trajectories.append(traj)
        else:
            print(traj, '\n is not valid')
    return trajectories, 0 if len(best_traj) == 0 else max([y for x,y in best_traj])


inp = pzzl(17, False).strings()[0].replace('target area: ', '')
xrange, yrange = inp_to_pars(inp)

vxmin =vminx(min(xrange))
vy0 = []
hymax = 0
for v in range(yrange[0], 1000):
    traj, valid = simulate(vxmin, v, *yrange, *xrange)
    if valid:
        vy0.append(v)
        hymx = max([xy[1] for xy in traj])
print(f'Max reachable height: {hymx} at vy0 = {vy0[-1]}')
combis = []
for vy in range(yrange[0], vy0[-1]+1):
    for vx0 in range(vxmin, xrange[1]+1):
        if simulate(vx0, vy, *yrange, *xrange)[1]:
            combis.append((vx0, vy))
print(len(combis))
